from datetime import datetime, timedelta

Fruta = ['Banana', 'Manzana', 'Pera', 'Uva', 'Naranja']

# Diccionario inicial con tiempos de pudrición
tiempos_pudricion = {
    'Banana': 7,
    'Manzana': 21,
    'Pera': 5,
    'Uva': 14,
    'Naranja': 21
}

def agregar_fruta(fruta, dias):
    tiempos_pudricion[fruta] = dias

def calcular_fecha_pudricion(fruta, fecha_actual):
    dias = tiempos_pudricion.get(fruta, None)
    if dias is None:
        return "Fruta no encontrada"
    fecha_pudricion = fecha_actual + timedelta(days=dias)
    return fecha_pudricion.strftime("%Y-%m-%d")

# Código funcional para calcular cuando se va a pudrir la fruta 

frutacalculada = input("Ingresa la fruta: ")

if frutacalculada in Fruta:
    agregar_fruta(frutacalculada, tiempos_pudricion[frutacalculada])
    fecha_actual = datetime.now()
    fecha_pudricion = calcular_fecha_pudricion(frutacalculada, fecha_actual)
    print(f"Tendrás que comprar {frutacalculada} nuevamente el {fecha_pudricion} o en {tiempos_pudricion[frutacalculada]} días para evitar que se pudra.")
    # Código funcional para agregar una nueva fruta junto a su tiempo de putrefacción
else:
    print("Fruta no encontrada. Proporcione el nombre y el tiempo de putrefacción en días de la fruta.")
    tiempos_pudricion[frutacalculada] = int(input('Ingresa los dias de putrefacción: '))
    agregar_fruta(frutacalculada, tiempos_pudricion[frutacalculada])
    fecha_actual = datetime.now()
    fecha_pudricion = calcular_fecha_pudricion(frutacalculada, fecha_actual)
    print(f"Tendrás que comprar {frutacalculada} nuevamente el {fecha_pudricion} para evitar que se pudra.")
    
    