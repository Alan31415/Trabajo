from datetime import datetime, timedelta

print('Bienvenido al programa para encargar el inventario necesario para le Fruteria grande X')

#LISTAS IMPORTANTES 
#Diccionario inicial con los tiempos de pudrición
tiempos_pudricion = {
    'Banana': 7,
    'Manzana': 21,
    'Pera': 5,
    'Uva': 14,
    'Naranja': 21
}
#La fruta necesita cambiar el precio dependiendo del precio del mercado 

#La cantidad de comprada y los clientes 
ClienteYcantidad = {
    "Juan": {"cantidad": 5,"producto": "Banana",},
    "Maria": {"cantidad": 3,"producto": "Manzana",},
    "Pedro": {"cantidad": 7,"producto": "Naranja",},
}



#Esta variable nos ayudara a saber si el usuario quiere anadir un nuevo cliente o no.


while True:
    print('  (1) Anadir un cliente \n  (2) Ver clientes existentes y sus pronosticos \n  (3) Modificar un producto \n  (4) Salir')
    
    instrucción = float(input('Que deseas hacer: '))
    
    if instrucción == 1:
        
        Añadir_clientes = input('Deseas anadir un nuevo cliente? ( Si la respuesta es no escibe Listo): ')
        def agregar_cliente():
            
            nombre = input("Ingrese el nombre del cliente: ")
            cantidad = float(input("Ingrese la cantidad de toneladas del producto: "))
            producto = input("Ingrese el producto: ")
        
            ClienteYcantidad[nombre] = {
            "cantidad": cantidad,
            "producto": producto,
            
            }
        
        agregar_cliente()
        
    if instrucción == 2:
        
        nombre_cliente = input('Como se llama el cliente: ')
        if nombre_cliente in ClienteYcantidad:
            
            datos = ClienteYcantidad[nombre_cliente]
            print(f"Datos de {nombre_cliente}:")
            for key, value in datos.items():
                
                print(f"  {key}: {value}")
        else:
            print(f"Cliente {nombre_cliente} no encontrado.")
            instrucción = input('Listo?: ')
        