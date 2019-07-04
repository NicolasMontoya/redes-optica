 ## Sistema de comunicacion optico simple

Este proyecto fue desarrollado para el curso de redes I - Universidad de Antioquia 2019, el objetivo de este proyecto es generar un algoritmo capaz de estructurar un protocolo de comunicación que transmita una imagen con símbolos predefinidos entre dos puntos lejanos mediante linternas. 

### Requisitos tecnicos

- Python 3
- Numpy
- Matplotlib
- OpenCV 3

### Procedimiento sugerido de instalacion (Linux con gestor de paquetes APT)

```bash
 sudo apt install python3
```
```bash
 sudo apt install python3-pip
```
```bash
 sudo apt install python3-opencv
```
```bash
 pip3 install matplotlib
```
```bash
 pip3 install numpy
```

### Descripcion de uso

Para el proyecto minimo se necesitan 4 personas, dos de estas como emisores y dos como receptores, los dos primeros tendran la labor de codificar la imagen en simbolos que entienda el sistema para luego enviar el codigo generado por el script mediante las linternas. Uno de los receptores debe estar atento al codigo transmitido mediante las linternas (Una linterna representa el 1 logico y la otra el 0 logico) mientras este va recibiendo los datos debe dictarselos al companero que tiene a su lado para que este los digite en el codigo del receptor y la imagen sea decoficada.



### Símbolos

Los símbolos definidos para transmitir la imagen son:

**Símbolo 0**

![Símbolo 0](https://a.imge.to/2019/07/05/4HQTs.png)

**Símbolo 1**

![Símbolo 1](https://a.imge.to/2019/07/05/4HzDk.png)

**Símbolo 2**

![Símbolo 2](https://a.imge.to/2019/07/05/4HMuH.png)

**Símbolo 3**

![Símbolo 3](https://a.imge.to/2019/07/05/4Hl1U.png)

**Símbolo 4**

![Símbolo 4](https://a.imge.to/2019/07/05/4HwOY.png)

**Símbolo 5**

![Símbolo 5](https://a.imge.to/2019/07/05/4H8PW.png)

**Símbolo 6**

![Símbolo 6](https://a.imge.to/2019/07/05/4HVkm.png)

**Símbolo 7**

![Símbolo 7](https://a.imge.to/2019/07/05/4HffC.png)

Cualquier imagen formada por dichos Símbolos puede ser transmitida.

## Protocolo

El protocolo usado maneja 12 bits distrubuidos de la siguiente manera:

1. Símbolo
2. Símbolo
3. Símbolo
4. Símbolo
5. paridad
6. size
7. size
8. size
9. checksum
10. checksum
11. checksum
12. checksum

Los primeros 4 bits son representan el numero del Símbolo a enviar, el quinto bit representa la paridad del sistema, la cual fue definida como par, los bits 6 7 y 8 son usados para indicar cuantas veces se repite un Símbolo y los ultimos bits son un sistema de verificacion por suma, dicho sistema funciona asi:

BITS Símbolo +  BITS CHECKSUM = 15

Para efectos practicos el codigo del trasmisor contiene un algoritmo que genera los bits a enviar, la unica responsabilidad del usuario (transmisor) es codificar la imagen en el archivo data.txt ubicado en la carpeta trasmisor

Ejm

1-7

Esto significa que el simbolo 1 se repetira siete veces.

2-4

Esto significa que el simbolo 2 se repetira cuatro veces.

**Nota:**  como se puede identificar en la definicion de los bits, el maximo numero de repeticiones por linea es 7, en caso de necesitar mas debe enviarse una linea mas.

### Uso

**Transmisor:** Para el transmisor primero codificamos la imagen en el archivo data.txt, luego corremos el siguiente comando ubicados en la raiz del proyecto:

```bash
python3 main.py mode=1 checksum=1
```

Dichon comando va a generar el codigo a transmitir mediante las linternas.

**Receptor:** Para el Receptor inicialmente corremos el siguiente script: 

```bash
python3 main.py mode=2 checksum=1
```
El codigo comenzara a pedir linea a linea los datos recibidos la comunicacion.
