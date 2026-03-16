print("Hola mundo desde python!!")

# Variables en Python

# número entero
Edad = 20

# número decimal
Precio = 50.5

# cadena de texto
Nombre = "Limber Limachi"

# valor booleano (verdadero o falso)
Bandera = True


# Mostrar valores
print("Nombre: ", Nombre)
print("Edad: ", Edad)
print("Precio: " + str(Precio))


# Entrada de datos
Nombre = input("Introduce tu nombre: ")
print("Hola " + Nombre)


# Suma de dos números ingresados por el usuario
Num1 = input("Ingresa el primer número: ")
Num2 = input("Ingresa el segundo número: ")
Suma = float(Num1) + float(Num2)
print("Resultado de la suma:", Suma)


# Manejo de cadenas
curso = "python para iniciantes"

print(curso.upper())       # convierte a mayúsculas
print(curso)               # muestra el texto original
print(curso.lower())       # convierte a minúsculas
print(curso.capitalize())  # primera letra en mayúscula


# Búsqueda dentro del texto
print(curso.find("h"))
print(curso.find("cia"))


# Reemplazo de texto
print(curso.replace("para", "FOR"))
print(curso)


# Verificar si una palabra está en el texto
print("for" in curso) 
print("para" in curso)
print("PARA" in curso)


# Operadores matemáticos básicos
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 4)

# división entera
print(10 // 4)

# residuo de una división
print(10 % 3)

# potencia
print(2 ** 4)


# Operadores de asignación
x = 10
x = x + 5
print(x)

y = 20
y += 5
print(y)

y = 20
y *= 5
print(y)


# Prioridad de operadores
x = 10 + 3 * 2
print(x)


# Comparaciones (True o False)
# >, >=, <, <=, ==, !=

x = 3 > 2
print(x)
 
x = 5 == 3
print(x)

x = 5 != 3
print(x)


# Operadores lógicos
# and, or, not

precio = 25
print(precio > 20 and precio < 30)

precio = 5
print(precio > 20 or precio < 30) 

print(not precio > 10)


# Condicionales
temperatura = int(input("Indica la temperatura: "))

if temperatura > 28:
    print("Hace calor")
elif temperatura > 20:
    print("El clima es agradable")
elif temperatura > 10:
    print("Hace algo de frío")
else:
    print("Hace frío")

print("Fin del proceso")


# Bucle while
contador = 12
while (contador <= 20):
    print(contador)
    contador += 1


# Imprimir asteriscos de forma creciente
i = 1
while (i <= 10):
    print(i * "*")
    i += 1
    
    
# LISTAS

frutas = ['Manzanas','Fresas','Naranjas','Peras','Maracuyás']

# Imprime toda la lista
print(frutas)

# Imprime el primer elemento
print(frutas[0])

# Error porque no existe esa posición
#print(frutas[5])

# Imprime el penúltimo elemento
print(frutas[-2])

# Imprime elementos dentro de ese rango
print(frutas[1:3])


# MÉTODOS DE LISTAS
numeros = [1,2,3,4,5]

# Agrega un elemento al final
numeros.append(6)

# Inserta elementos en posiciones específicas
numeros.insert(0,-1)
numeros.insert(1,0)

# Elimina un elemento específico
numeros.remove(1)

# Verifica si un número está en la lista
print(3 in numeros)

# Tamaño de la lista
print(len(numeros))

# Elimina todos los elementos
numeros.clear()
print(numeros)



# OBJETO RANGE

# Crea una secuencia de números
numeros = range(3)

# Convertir la secuencia en lista
numeros = list(range(3))

# Recorrer la secuencia
for item in numeros:
    print(item)

# Secuencia del 5 al 9
for item in range(5,10):
    print(item)

# Secuencia con salto de 2
for item in range(10,20,2):
    print(item)

print(numeros)



# TUPLAS (no se pueden modificar)

numeros = (1,2,5,4,5,6)

# Mostrar elemento en una posición
print(numeros[3])

# Contar cuántas veces aparece un número
print(numeros.count(5))

# Buscar posición de un elemento
print(numeros.index(2))
print(numeros.index(5))



# DICCIONARIOS (clave - valor)

mi_diccionario = {'nombre':'Bruno Diaz','edad':25,'Ciudad':'La Paz'}

# Mostrar todo el diccionario
print(mi_diccionario)

# Acceder a valores
print(mi_diccionario['nombre'])
print(mi_diccionario['Ciudad'])

# Agregar un nuevo elemento
mi_diccionario['profesion'] = 'Ingeniero'

# Eliminar un elemento
del mi_diccionario['Ciudad']
print(mi_diccionario)

# Mostrar las claves
print(mi_diccionario.keys())

# Mostrar los valores
print(mi_diccionario.values())

# Verificar si existe una clave
if 'edad' in mi_diccionario:
    print('Clave encontrada')

if 'ciudad' in mi_diccionario:
    print('Clave encontrada')

# Recorrer el diccionario
for clave,valor in mi_diccionario.items():
    print('clave: ',clave,' valor: ',valor)



# FUNCIONES

# Función sin parámetros
def Saludar():
    print('Hola, bienvenidos al curso de Python')

Saludar()
Saludar()

# Función con parámetro
def saludo(nombre):
    print('Hola '+nombre+' bienvenido a clases')

saludo('Limber')
saludo('Helen')


# Función que devuelve un valor
def suma(a,b):
    return a+b

resultado = suma(10,4)
print("Resultado:",resultado)


# Parámetro con valor por defecto
def bienvenida(nombre='Estudiante'):
    print("Bienvenido, ",nombre)

bienvenida()
bienvenida("Susana")


# Función con cantidad variable de argumentos
def sumador(*args):
    return sum(args)

print(sumador(1,2,3,4,5))
print(sumador(4,5,6))