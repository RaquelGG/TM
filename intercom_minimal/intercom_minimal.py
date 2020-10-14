import sounddevice as sd
import threading
from udp_send import UdpSender
from udp_receive import UdpReceiver
import numpy
assert numpy

def record(chunk_size, stream):
    stream.start()
    chunk, _ = stream.read(chunk_size)
    return chunk
        
def pack(chunk):
    '''
    TODO 
    '''
    return chunk

def unpack(packed_chunk):
    '''
    TODO
    '''
    return packed_chunk

def play(chunk, stream):
    stream.write(chunk)
    #print("Received chunk")
    #print(chunk)

def cliente():
    stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')
    stream.start()
    with UdpReceiver() as receiver:
        while True:
            packed_chunk = receiver.receive()
            chunk = unpack(packed_chunk)
            play(chunk, stream)

def servidor():
    CHUNK_SIZE = 64
    DESTINATION = 'localhost'
    stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')

    with UdpSender() as sender:
        while True:
            chunk = record(CHUNK_SIZE, stream)
            packed_chunk = pack(chunk)
            sender.send(packed_chunk, DESTINATION)


if __name__ == "__main__":
    client = threading.Thread(target=cliente)
    server = threading.Thread(target=servidor)

    client.start()
    server.start()