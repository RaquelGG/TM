
import sounddevice as sd
from udp_receive import UdpReceiver
import numpy
assert numpy

def unpack(packed_chunk):
    '''
    TODO
    '''
    return packed_chunk

def play(chunk, stream):
    stream.write(chunk)
    print("Received chunk")
    print(chunk)

if __name__ == "__main__":
    stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')
    stream.start()
    with UdpReceiver() as receiver:
        while True:
            packed_chunk = receiver.receive()
            chunk = unpack(packed_chunk)
            play(chunk, stream)