"""
Calcular la hora correspondiente al segundo anterior
"""

# Entradas
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# Proceso
segundos -= 1
if segundos < 0:
    segundos = 59
    minutos -= 1
    if minutos < 0:
        minutos = 59
        horas -= 1
        if horas < 0:
            horas = 23
tiempo = f'{horas:02d}:{minutos:02d}:{segundos:02d}'

# Salidas
print('Hora al segundo anterior >', tiempo)