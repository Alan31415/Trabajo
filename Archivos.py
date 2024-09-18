import csv

notas = open("notas.txt", "w")
notas.write("10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n")

notas.close()

notas = open("notas.txt", "a")
notas.write("10\n9\n8\n7\n6\n5\n4\n3\n2\n10")
notas.close()

nombre = ["pedro", "maria", "jose"]
nombres = open("nombres.txt", "w")

for i in nombre:
    nombres.write(i + "\n")

nombres.close()


datos = [
    ["manzana", 34 ,10],["banana ", 20 ,9],["naranja",12 , 8]]

nombreArchivo = open("productos.csv", "w")
csv.writer(nombreArchivo).writerows(datos)