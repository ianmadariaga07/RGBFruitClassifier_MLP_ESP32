import serial
import time
import joblib
import warnings
warnings.filterwarnings("ignore")

#configuracion puerto serial
PUERTO = '/dev/ttyACM0' 
BAUDIOS = 115200

print("Cargando modelo")
try:
    clf = joblib.load('modeloFrutasTanh.pkl')
    print("Modelo cargado")
except:
    print("ERROR: No se encontro 'modeloFrutasTanh.pkl'")
    exit()
#conexion
try:
    arduino = serial.Serial(PUERTO, BAUDIOS, timeout=1)
    time.sleep(2) 
    print(f"Conectado a {PUERTO}")
except:
    print(f"No se pudo conectar a {PUERTO}. Cierra el Arduino")
    exit()

print("\n--- INICIANDO DETECCIÓN EN TIEMPO REAL ---")
print("Presionar Ctrl + C para detener.\n")
arduino.reset_input_buffer()

while True:
    try:
        #leer línea 
        linea = arduino.readline().decode('utf-8').strip()
        if linea:
            datos = linea.split(',')
            if len(datos) == 3:
                r = float(datos[0])
                g = float(datos[1])
                b = float(datos[2])
                
                prediccion = clf.predict([[r, g, b]])[0] 
                mensaje_log = f"R:{int(r)} G:{int(g)} B:{int(b)} --> "
                
                #VAmos a enviar M, L, P, Z, C o N al arduino
                if prediccion == 'manzana':
                    print(mensaje_log + "MANZANA")
                    arduino.write(b'M') 
                elif prediccion == 'limon':
                    print(mensaje_log + "LIMON")
                    arduino.write(b'L')
                elif prediccion == 'platano':
                    print(mensaje_log + "PLATANO")
                    arduino.write(b'P')
                elif prediccion == 'zanahoria':
                    print(mensaje_log + "ZANAHORIA")
                    arduino.write(b'Z')
                elif prediccion == 'cebolla':
                    print(mensaje_log + "CEBOLLA")
                    arduino.write(b'C')
                else: 
                    print(mensaje_log + "NO HAY NADA...")
                    arduino.write(b'N')
    except KeyboardInterrupt:
        print("\nDeteniendo")
        break
    except Exception as e:
        print(f"Error: {e}")
arduino.close()
print("Desconectado")