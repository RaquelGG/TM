import sounddevice as sd
import threading
from udp_send import UdpSender
from udp_receive import UdpReceiver
import numpy
assert numpy

class InterCom():
    # Audio defaults
    # 1 = mono, 2 = stereo
    NUMBER_OF_CHANNELS = 2
    FRAMES_PER_SECOND  = 44100
    FRAMES_PER_CHUNK   = 1000
    
    # Network defaults
    PAYLOAD_SIZE = 1024
    IN_PORT     = 4444
    OUT_PORT    = 4444
    ADDRESS     = 'localhost'

    lock = threading.Lock()

    def record(self, chunk_size, stream):
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
            
    def pack(self, chunk):
        """TODO
            """
        return chunk

    def unpack(self, packed_chunk):
        """TODO
            """
        return packed_chunk

    def play(self, chunk, stream):
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

    def client(self):
        stream = sd.RawStream(samplerate=self.FRAMES_PER_SECOND, channels=self.NUMBER_OF_CHANNELS, dtype='int16')
        stream.start()
        with UdpReceiver() as receiver:
            while True:
                packed_chunk = receiver.receive()
                chunk = self.unpack(packed_chunk)
                self.lock.acquire()
                self.play(chunk, stream)
                self.lock.release()

    def server(self):
        stream = sd.RawStream(samplerate=self.FRAMES_PER_SECOND, channels=self.NUMBER_OF_CHANNELS, dtype='int16')
        stream.start()
        with UdpSender() as sender:
            while True:
                self.lock.acquire()
                chunk = self.record(self.FRAMES_PER_CHUNK, stream)
                self.lock.release()
                packed_chunk = self.pack(chunk)
                sender.send(packed_chunk, self.OUT_PORT, self.ADDRESS)

if __name__ == "__main__":
    intercom = InterCom()
    clientT = threading.Thread(target=intercom.client)
    serverT = threading.Thread(target=intercom.server)

    clientT.start()
    serverT.start()