def interfaz_investigador():
    print("=== SISTEMA EXPERTO: ANÁLISIS DE PRECISIÓN ===")
    
    # 1. Interacción inicial (El usuario define el objetivo)
    objetivo_usuario = float(input("Ingrese el ángulo objetivo para la prueba (0-360): "))
    memoria_trabajo["angulo_objetivo"] = objetivo_usuario
    
    # 2. Adquisición y Filtrado
    dato_crudo = leer_sensor_encoder()
    dato_procesado = procesar_datos_adquisicion(dato_crudo)
    memoria_trabajo["angulo_real"] = dato_procesado
    
    # 3. Procesamiento (Motor de Inferencia)
    diagnostico, comando = motor_de_inferencia(memoria_trabajo, reglas_precision)
    
    # 4. Salida e Interacción (Resultados y Explicación)
    print("\n--- RESULTADOS ---")
    print(f"Diagnóstico emitido: {diagnostico}")
    print(f"Acción recomendada: {comando}")
    
    solicitar_explicacion = input("\n¿Desea ver la justificación del sistema? (s/n): ")
    if solicitar_explicacion.lower() == 's':
        explicacion = generar_explicacion(memoria_trabajo, diagnostico, reglas_precision["tolerancia_maxima"])
        print(f"\n{explicacion}")

# Ejecutar la interfaz
# interfaz_investigador()