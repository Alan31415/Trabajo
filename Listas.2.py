#Ejercicio 1 

palabras = ['casa', 'python', 'perro' , 'gato', 'hola', 'python']

for i in palabras:
    if i == 'python':
        python = palabras.count('python')
print(f'La palabra python se repite {python} veces') 

#Ejercicio 2

frases = ['casa', 'python', 'perro' , 'gato', 'hola', 'python']

print(frases)

frases [0], frases [1], frases[2], frases[3], frases[4], frases[5] = 'CASA', 'PYTHON', 'PERRO', 'GATO', 'HOLA', 'PYTHON'

print(frases)

#Ejercicio 3

oraciones = ['casa', 'python', 'perro' , 'gato', 'hola', 'python', 'tu', 'yo', ]

for oración in oraciones[:]:
    
    if len(oración) < 4:
        oraciones.remove(oración)
        
print(oraciones)

#Ejercicio 4

numeros = [1, 15 , 83, 94, 134, 576, 174, 172, 185, 183]
numero_mayor = numeros[0]
for numero in numeros:
    
    if numero > numero_mayor:
        numero_mayor = numero
    else:
        print(f'El numero {numero} no es el mayor en la lista')

print(numero_mayor)

#Ejercicio 5

numeros1 = [-1, 15 , -83, 94, -134, 576, -174, 172, -185, 183]
numeros_positivos = 0
for numero in numeros1[:]:
    if numero < 0:
        print(f'El numero {numero} es negativo')
    else:
        
        numeros_positivos += 1
        print(f'El numero {numero} es positivo')
        print(f'Hay {numeros_positivos} positivos en la lista')
        
#Ejercicio 6

Lista = [1,2,3,4,5]

Lista_Invertida = Lista[::-1]

print(Lista_Invertida)


#Ejercicio 7

Lista = [1,2,3,4,5]

Numero_De_Elementos = len(Lista)

promedio = sum(Lista)/ Numero_De_Elementos

print(promedio)
