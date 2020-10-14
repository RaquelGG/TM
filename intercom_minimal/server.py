#!/usr/bin/env python3
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
    """Write samples to the stream.

        Parameters
        ----------
        chunk : buffer
            A buffer of interleaved samples. The buffer contains
            samples in the format specified by the *dtype* parameter
            used to open the stream, and the number of channels
            specified by *channels*.

        stream : sd.RawStream
            Raw stream for playback and recording.
        """
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