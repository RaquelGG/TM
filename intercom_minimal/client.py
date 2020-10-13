import sounddevice as sd
from udp_send import UdpSender
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

if __name__ == "__main__":
    CHUNK_SIZE = 64
    DESTINATION = 'localhost'
    stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')

    with UdpSender() as sender:
        while True:
            chunk = record(CHUNK_SIZE, stream)
            packed_chunk = pack(chunk)
            sender.send(packed_chunk, DESTINATION)