def procesar_datos_adquisicion(lectura_cruda):
    """
    Control de coherencia y transformación de datos.
    """
    # Validar que el dato esté en el rango de 12 bits
    if lectura_cruda < 0 or lectura_cruda > 4095:
        raise ValueError("Lectura anómala del sensor. Dato descartado.")
    
    # Transformar a grados (360 / 4096 = 0.0878 grados por paso)
    grados_actuales = lectura_cruda * (360.0 / 4096.0)
    
    # Redondear a dos decimales para el análisis de precisión
    return round(grados_actuales, 2)