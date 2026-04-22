def generar_explicacion(memoria, conclusion, tolerancia):
    """
    Rastrea la lógica y justifica la conclusión.
    """
    reporte = (
        f"--- REPORTE DE EXPLICACIÓN ---\n"
        f"El sistema determinó el siguiente estado: '{conclusion}'.\n"
        f"Razón: El ángulo objetivo era {memoria['angulo_objetivo']}° "
        f"y el encoder registró {memoria['angulo_real']}°. "
        f"Esto genera una desviación de {memoria['desviacion']}°, "
        f"evaluada bajo el umbral de tolerancia estricta de {tolerancia}°."
    )
    return reporte