def analizar_estacionamiento():
    # Inicializar variables
    horas = 12
    total_autos = 0
    max_autos_por_hora = 50
    horas_concurrencia = {}
    estacionamiento_lleno = False
    estacionamiento_vacio = True

    # Loop para ingresar la cantidad de autos por hora
    for hora in range(1, horas + 1):
        while True:
            try:
                autos = int(input(f"Ingrese la cantidad de autos estacionados en la hora {hora}: "))
                if 0 <= autos <= max_autos_por_hora:
                    break
                else:
                    print("La cantidad de autos debe estar entre 0 y 50.")
            except ValueError:
                print("Ingrese un número válido.")

        # Actualizar total de autos
        total_autos += autos

        # Verificar si el estacionamiento estuvo lleno o vacío en algún momento
        if autos > 0:
            estacionamiento_vacio = False
        if autos == max_autos_por_hora:
            estacionamiento_lleno = True

        # Guardar la cantidad de autos por hora
        horas_concurrencia[hora] = autos

    # Calcular el promedio de autos
    promedio_autos = total_autos / horas

    # Encontrar las 3 horas con mayor concurrencia
    horas_mas_concurridas = sorted(horas_concurrencia, key=horas_concurrencia.get, reverse=True)[:3]

    # Mostrar resultados
    print("\nResultados:")
    print(f"A) El promedio de autos de la jornada es: {promedio_autos:.2f}")
    print(f"B) Las 3 horas con mayor concurrencia fueron: {horas_mas_concurridas}")
    print(f"C) El estacionamiento {'estuvo lleno' if estacionamiento_lleno else 'estuvo vacío' if estacionamiento_vacio else 'tuvo diferentes niveles de ocupación'}.")

# Llamar a la función para ejecutar el programa
analizar_estacionamiento()
