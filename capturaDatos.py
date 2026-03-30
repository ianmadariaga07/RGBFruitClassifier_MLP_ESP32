import serial
import csv
import time
import os

#configuracion puerto serial
PUERTO = '/dev/ttyACM0'  
BAUDIOS = 115200
archivos = {
    'prueba':'prueba.csv',
    'manzana':'manzana.csv',
    'limon':'limon.csv',
    'nada':'nada.csv',
    'platano':'platano.csv',
    'zanahoria':'zanahoria.csv',
    'cebolla':'cebollamorada.csv'
}

try:
    arduino = serial.Serial(PUERTO, BAUDIOS, timeout=1)
    time.sleep(2) 
    print(f"Conectado a {PUERTO}")
except:
    print(f"No se pudo conectar al puerto {PUERTO}")
    exit()

print("\nRECOLECCION DE DATOS ")
print("Instrucciones:")
print("Pon la fruta frente al sensor y escribe la etiqueta")
print("  Usa: 'manzana', 'limon', 'platano', 'zanahoria', 'cebolla' o 'nada'.")
print("Escribe salir para terminar.\n")


while True:
    etiqueta = input("Objeto que se va a escanear (manzana/limon/platano/zanahoria/cebolla/nada): ").lower()
    if etiqueta == 'salir':
        break
    if etiqueta not in archivos:
        print("Etiqueta no valida")
        continue

    archivoActual = archivos[etiqueta]
    if not os.path.isfile(archivoActual):
        with open(archivoActual, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['R','G','B','Etiqueta'])

    print(f"Recolectando datos para: {etiqueta.upper()} en {archivoActual}...")
    muestrasTomadas = 0
    arduino.reset_input_buffer()
    #TOMAMOS 100 LECTURAS
    while muestrasTomadas < 100: 
        try:
            linea = arduino.readline().decode('utf-8').strip()
            if linea:
                datos = linea.split(',')
                if len(datos) == 3:
                    with open(archivoActual, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([datos[0], datos[1], datos[2], etiqueta])
                    
                    print(f"Muestra {muestrasTomadas+1}/100: {linea} -> {etiqueta}")
                    muestrasTomadas += 1
        except Exception as e:
            print(f"Error de lectura: {e}")
    print("Guardado con exito\n")

arduino.close()
print("Conexión cerrada")