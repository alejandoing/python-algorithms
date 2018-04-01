# Python Algorithms

<p align="justify">
<i>Python Algorithms</i> es un conjunto de scripts escritos en Python que realizan diferentes funciones, desde encriptado y desencriptado de cadenas de texto hasta algoritmos base de Machine Learning como Regresión Lineal. Pueden ser ejecutados en cualquier sistema operativo que tenga instalado Python 2.6 o superarior. Este proyecto sirve como punto de partido para futuros desarrollos complejos con el lenguaje. Es importante mencionar que el programa tiene una entrada única en el archivo <i>main.py</i>. Allí aparece un pequeño menú para seleccionar el algoritmo que se quiere ejecutar y siempre podrás navegar a travé de los diferentes scripts sin necesidad de detener la ejecución. Todos están corriendo en un bucle dentro del archivo <i>main.py</i>.
</p>

<p align="center">
  <img src="https://taufanlubis.files.wordpress.com/2011/02/python01.png"/>
</p>

[![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/)
[![python](https://img.shields.io/badge/python-2.6%2B-blue.svg)](https://python.org/)

## Cryptography

*Cryptograhy* es un algoritmo que se encarga de realizar un proceso de encriptado y desencriptado binario.

### 1. Cypher

<p align="justify">
La función de encriptado traduce, cualquier cadena de texto previamente ingresada por el usuario, en código de máquina. El proceso es simple, los datos del input ingresan a un función que, a traves de diferentes comandos y transformación de formato, retorna un mensaje con el código binario correspondiente. En este caso se dividen las palabras y se guardan en una lista para luego ser transformadas en cada iteración. Al final se unifican todos los resultados y se muestran en pantalla. El proceso no suele tardar más de un segundo y es posible escribir cualquier cantidad de texto.
</p>

### 2. Decypher

<p align="justify">
La función de desencriptado realiza el proceso inverso, al introducir un código binario, es capaz de retornar una cadena de texto entendible por el lenguaje humano. El proceso comienza obteniendo los datos del input y transformando mendiante diferentes comando el formato ingresado. En este caso se dividen los bytes y se guardan en una lista para luego ser transformados en cada iteración. Al final se unifican todos los resultados y se muestran en pantalla. De igual manera, el tiempo de respuesta es inmediato y es posible escribir cualquier cantidad de código binario.
</p>

## Binary Search

<p align="justify">
<i>Binary Search</i> es un algortimo que se encarga de realizar una búsqueda inteligente de un elemento dentro de una lista de números secuenciales. El usuario tendrá la posibilidad de ingresar una lista de números manualmente o podrá optar por utilizar el mecanismo de generación automática de una lista de números aletorios. Posterior a la escogencia de una de las dos opciones disponibles deberá ingresar un número a buscar dentro de la lista. El algoritmo comienza a funcionar: por cada iteración se reduce a la mitad el rango de búsqueda y retorna un mensaje en pantalla. Finalmente, se notifica al usuario si la búsqueda ha tenido éxito o no. También se especifica la duración en segundos que ha tomado todo el proceso.
</p>

## Variance and Deviation Standard

<p align="justify">
<i>Variance and Deviation Standard</i> es un algoritmo que se encarga de obtener, en primera instancia, una variable aleatoria, que en teoría de probabilidad se conoce como <i>Varianza</i>, representa una medida de dispersión definida como la esperanza del cuadrado de la desviación de dicha variable respecto a su media. O en pocas palabras, la media de los residuos al cuadrado. La <i>Varianza</i> se obtiene a partir de su formula genérica. El método recibe una lista de números y realiza las operaciones matemáticas correspondientes hasta retornar el resultado correspondiente.
</p>

<p align="justify">
Por otro lado, el algoritmo adicionalmente tiene la funcionalidad de obtener la <i>Desviación Estándar</i> o <i>Desviación Típica</i>, una medida de dispersión para variables de razón (variables cuantitativas o cantidades racionales) y de intervalo. Se define como la raíz cuadrada de la varianza de la variable. Este método se ejecuta justo después de obtener la <i>Varianza</i> y recibe como parámetro el resultado de la anterior operación y la lista de números. Se encarga de aplicar la formula matemática genérica y luego retornar el resultado final en pantalla.
</p>

## Contact Book

<p align="justify">
<i>Contact Book</i>, tal como su nombre lo indica, emula algunas funcionalidades de una sencilla agenda de contactos. En primera luego se puede agregar un contacto con los atributos: nombre, teléfo e email. Luego tenemos el resto de las opciones CRUD (leer, actualizar y eliminar). Es posible realizar una búsqueda a partir del nombre de contacto. El programa no permite el registro de dos contactos con el mismo nombre. Ahora bien, además de realizar todas las opciones comunes de una entidad, se habilita la posibilidad de mantener los datos en el tiempo a traves de métodos de lectura y escritura de archivos .CSV. En pocas palabras, <i>Contact Book</i> trabaja con una pequeña base de datos. 
</p>

## Hanged

<p align="justify">
<i>Hanged</i> es un divertido algoritmo que se encarga de emular el funcionamiento del popular juego de palabras <i>El Ahorcado</i>. Al ingresar se genera una palabra secreta aleatoriamente a partir de una lista previamente establecida. El objetivo es descubrir la palabra secreta con la menor cantidad de intentos fallidos. En cada iteración el usuario deberá ingresar una letra y de ser correcta aparecerá impresa en el lugar correspondiente dentro de la palabra. En caso de intentar con una letra incorrecta la interfaz de juego se actualizará a un dibujo cada vez más cercano al de un hombre ahorcado en un árbol. Los dibujos están creados a partir de la técnica de <i>Arte ASCII</i>. El algoritmo además imprime la lista de letras utilizadas y los intentos realizados. Finalmente, al finalizar el juego el usuario tiene la posibilidad de intentar nuevamente o regresar al menú principal.
</p>

## Fibonacci

<p align="justify">
<i></i>
</p>

## Linear Regression

<p align="justify">
<i></i>
</p>

## Licencia

[![python](https://img.shields.io/npm/l/express.svg)](https://www.python.org/)
