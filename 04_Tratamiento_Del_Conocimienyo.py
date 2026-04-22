def motor_de_inferencia(memoria, reglas):
    """
    Aplica las reglas sobre los hechos actuales para sacar una conclusión.
    """
    objetivo = memoria["angulo_objetivo"]
    real = memoria["angulo_real"]
    
    # Calcular el hecho derivado
    desviacion = abs(objetivo - real)
    memoria["desviacion"] = desviacion
    
    # Inferencia lógica
    if desviacion <= reglas["tolerancia_maxima"]:
        conclusion = reglas["estado_optimo"]
        accion = "Continuar ciclo de prueba."
    elif desviacion > reglas["tolerancia_maxima"] and desviacion < 2.0:
        conclusion = reglas["error_holgura"]
        accion = "Registrar anomalía leve y recalibrar PID."
    else:
        conclusion = reglas["error_ruido"]
        accion = "Detener prueba. Revisar conexiones físicas."
        
    return conclusion, accion