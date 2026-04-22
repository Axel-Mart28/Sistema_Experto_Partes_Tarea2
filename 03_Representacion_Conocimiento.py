# BASE DE CONOCIMIENTO (Reglas estáticas del experto)
reglas_precision = {
    "tolerancia_maxima": 0.5, # Grados de error permitidos
    "error_holgura": "Posible holgura mecánica en los engranajes",
    "error_ruido": "Ruido eléctrico en la señal del encoder",
    "estado_optimo": "Precisión dentro de los parámetros de la investigación"
}

# BASE DE HECHOS (Memoria de trabajo temporal)
memoria_trabajo = {
    "angulo_objetivo": 90.0, # A dónde queremos llegar
    "angulo_real": None,     # Dato que llenará el sensor
    "desviacion": None       # Calculado por el motor
}