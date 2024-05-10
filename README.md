# examen-parcial-algoritmos-2

# Ejercicio 1 : #Spotify
Este proyecto contiene dos archivos:
1. `genre.py`: Este archivo define la clase `Genre`, que es una enumeración de géneros musicales como `ROCK`, `POP`, `EDM` y `COUNTRY`.
2. `song.py`: Este archivo contiene la clase `Song`, que se utiliza para representar canciones. La clase `Song` tiene propiedades como nombre, artista, duración, fecha de lanzamiento y géneros. Esta clase también tiene métodos para obtener y modificar estas propiedades, así como métodos para agregar géneros adicionales, verificar la igualdad entre canciones y representar la canción como una cadena legible para humanos.


# Ejercicio 2 : Recursividad: Cálculo del Factorial
# Cálculo del Factorial de un Número
Esta función calcula el factorial de un número entero dado utilizando recursión.

### Codigo de la funcion 
def factorial(n):
if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

## Función factorial
La función `factorial(n)` calcula el factorial del número entero `n` proporcionado como argumento. 

### Parámetros
- `n` : int
  Número entero al que se le calculará el factorial.

### Retorna
- `int`
  El factorial del número dado.


# Ejercicio 3 : explicacion de Bubble Sort : 
## Bubble Sort

El método de ordenación Bubble Sort, es uno de los algoritmos más simples para ordenar elementos en una lista. Funciona comparando pares de elementos adyacentes y, si están en el orden incorrecto, los intercambia. Este proceso se repite hasta que no se necesitan más intercambios, lo que indica que la lista está ordenada.

**Funcionamiento:**
1. Comienza comparando el primer par de elementos de la lista.
2. Si el primer elemento es mayor que el segundo, los intercambia.
3. Luego, pasa al siguiente par de elementos y repite el proceso hasta el final de la lista.
4. Este proceso se repite para cada elemento de la lista, lo que provoca que los elementos más grandes "burbujeen" hacia el final de la lista en cada iteración.
5. Finalmente, cuando no se realizan intercambios en una iteración completa, la lista está ordenada.

**Cuándo utilizar Bubble Sort:**
Bubble Sort es útil principalmente para listas pequeñas o cuando la implementación de otros algoritmos más eficientes no es viable. Debido a su complejidad de tiempo de O(n^2), donde n es el número de elementos en la lista, no es eficiente para listas grandes.

**Ejemplo conceptual:**
Tomemos la lista `[34, 7, 23, 32, 5]` como ejemplo para ilustrar el funcionamiento del Bubble Sort:

1. Comenzamos comparando 34 y 7. Como 34 es mayor que 7, los intercambiamos: `[7, 34, 23, 32, 5]`.
2. Luego, comparamos 34 y 23. Intercambio necesario: `[7, 23, 34, 32, 5]`.
3. Continuamos con 34 y 32. Intercambio necesario: `[7, 23, 32, 34, 5]`.
4. Ahora, comparamos 34 y 5. Intercambio necesario: `[7, 23, 32, 5, 34]`.
5. En la primera iteración, el elemento más grande (34) ha "burbujeado" hacia el final de la lista.
6. Repetimos este proceso hasta que no se necesiten más intercambios. En este caso, al repetirlo, los numeros mayores de 5 van a ir burbujeando al final, en este caso sabemos que necesitamos 3 interaciones mas para que el 5 este el primero y la lista este completamente ordenada.


# Ejercicio 4 : Functools
# unciones de la Clase `SimpleOperations`
La clase `SimpleOperations` proporciona dos métodos para calcular precios finales:

## 1. `apply_discount(self, price, discount):`
- Este método aplica un descuento al precio dado y devuelve el nuevo precio.
- **Parámetros:**
  - `price`: El precio base al que se aplicará el descuento.
  - `discount`: El porcentaje de descuento como un decimal.
- **Retorna:** El precio después de aplicar el descuento.

## 2. `calculate_tax(self, price, tax_rate):`
- Este método calcula y agrega el impuesto al precio dado.
- **Parámetros:**
  - `price`: El precio base al que se aplicará el impuesto.
  - `tax_rate`: El porcentaje de impuesto como un decimal.
- **Retorna:** El precio después de agregar el impuesto.




