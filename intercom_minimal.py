import sounddevice as sd
import numpy
assert numpy

class SequentialInterCom:
    def record_io_and_play(self):
        """
        docstring
        """
        CHUNK_SIZE = 64
        # Grabar y enviar
        chunk = self.record(CHUNK_SIZE)
        packed_chunk = self.pack(chunk)
        self.send(packed_chunk)

        # Recibir y reproducir
        packed_chunk = self.receive()
        chunk = self.unpack(packed_chunk)
        self.play(chunk)



    def record(self, chunk_size: int):
        stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')
        stream.start()

        chunk, _ = stream.read(chunk_size)
        return chunk
        
    def pack(self, chunk):
        return chunk
    
    def send(self, packed_chunk):
        pass

    def receive(self):
        pass

    
    