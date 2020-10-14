import sounddevice as sd
import threading
from udp_send import UdpSender
from udp_receive import UdpReceiver
import numpy
assert numpy

def record(chunk_size, stream):
    """Record a chunk from the stream into a buffer.

        Parameters
        ----------
        chunk_size : int
            The number of frames to be read.

        stream : buffer
            Raw stream for playback and recording.

        Returns
        -------
        chunk : sd.RawStream
            A buffer of interleaved samples. The buffer contains
            samples in the format specified by the *dtype* parameter
            used to open the stream, and the number of channels
            specified by *channels*.
        """

    chunk, _ = stream.read(chunk_size)
    return chunk
        
def pack(chunk):
    """TODO
        """
    return chunk

def unpack(packed_chunk):
    """TODO
        """
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

def client():
    stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')
    stream.start()
    with UdpReceiver() as receiver:
        while True:
            packed_chunk = receiver.receive()
            chunk = unpack(packed_chunk)
            play(chunk, stream)

def server():
    CHUNK_SIZE = 64
    DESTINATION = 'localhost'
    stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')
    stream.start()
    with UdpSender() as sender:
        while True:
            chunk = record(CHUNK_SIZE, stream)
            packed_chunk = pack(chunk)
            sender.send(packed_chunk, DESTINATION)


if __name__ == "__main__":
    client = threading.Thread(target=client)
    server = threading.Thread(target=server)

    client.start()
    server.start()