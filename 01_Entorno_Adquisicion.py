import random

def leer_sensor_encoder():
    """
    Simula la lectura cruda de un encoder magnético de 12 bits (0 a 4095).
    """
    # En un caso real: puerto_serial.readline()
    lectura_cruda = random.randint(0, 4095) 
    return lectura_cruda