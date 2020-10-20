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
	- En una sola linea
	- En varias lineas
		"""Al inicio del "docstringt" aparecera una linea de resumen siguiendo las 3 comillas o en la siguiente linea, 

		   pero tras ella se dejara una linea en blanco, seguido por una descripción más elaborada. 



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
