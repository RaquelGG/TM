# Tecnologías multimedia
Proyecto de tecnologías multimedia consistente en un interfono cliente/servidor que empaqueta trozos de audio, los envía por UDP y los reproduce con la menor latencia posible.

## Guia de buenas practicas utilizadas

El uso de buenas practicas permite a los diferentes usuarios ya sean o no parte de nuestro proyecto tener una mayor compresión sobre su contenido evitando rompeduras de cabeza innecesarias.

En python existe una guia de buenas practicas, denominada PEP 8. Esta define por convenio el estilo que se ha de usar para la asignación de nombres a los metodos, la documentación, la importacíón de clases, etc...


### Clases
Las clases deben utilizar por convención el formato "CapWords", palabras que siempre comienzan con mayusculas. [PEP-0008](https://www.python.org/dev/peps/pep-0008).

```python
class UdpReceiver():
    pass
```


### Métodos y variables
Los nombres de los metodos y las instancias de las variables usan "_" (barrabaja) entre las palabras, siendo el numero de estas las necesarias para su comprensión. En el caso de las 
```python
def disponible_args():
    NUMBER_OF_CHANNELS = 2
```


### Docstring
La creación de documentación usa otro convenio definido por PEP 257.
El convenio define las lineas de documentación como "docstrings" y deben de ser escritos para todo el contenido publico como modulos, funciones, clases y metodos, en el caso del contenido no publico no sera necesario, pero si sera necesario escribir una linea explicando que hace el metodo. 

Todo el contenido que se utilice como "docstring" debe de aparecer debajo de la linea "def", el formato para hacerlo es usar """triples comillas""". Existen dos formas de usar "docstring":
-   En una sola linea
-   En varias lineas: Al inicio del "docstringt" aparecera una linea de resumen siguiendo las 3 comillas o en la siguiente linea, pero tras ella se dejara una linea en blanco, seguido por una descripción más elaborada.



[1] PEP 257. <https://www.python.org/dev/peps/pep-0257/>
[2] PEP 8. <https://www.python.org/dev/peps/pep-0008/>

```python
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
```

## Cosas a destacar sobre la implementación
Se ha usado la biblioteca [`sounddevice`](https://python-sounddevice.readthedocs.io/en/0.4.1/) para la captura y reproducción del audio.
### RawInputStream y RawOutputStream
[`RawInputStrea`](https://python-sounddevice.readthedocs.io/en/0.4.1/api/raw-streams.html#sounddevice.RawInputStream) gestiona los dispositivos de entrada de nuestro dispositivo y [`RawOutputStrea`](https://python-sounddevice.readthedocs.io/en/0.4.1/api/raw-streams.html#sounddevice.RawOutputStream) los de salida.
```python
stream = sd.RawInputStream(samplerate=self.frames_per_second, channels=self.number_of_channels, dtype='int16')
...
stream = sd.RawOutputStream(samplerate=self.frames_per_second, channels=self.number_of_channels, dtype='int16')
```
Como tratamos la entrada y la salida totalmente por separado, no es necesario realizar exclusión mutua.

### Hilos
Usamos la biblioteca [`threading`](https://docs.python.org/3.8/library/threading.html) que construye interfaces de subprocesamiento de nivel superior sobre el módulo `_thread` de nivel inferior.

```python
import threading
... 
clientT = threading.Thread(target=intercom.client)
clientT.start()
```
