def analizar_estacionamiento():
    # Inicializar variables
    horas = 12
    total_autos = 0
    max_autos_por_hora = 50
    horas_concurrencia = []
    horas_vacias = []
    horas_lleno = []

    # Loop para ingresar la cantidad de autos por hora
    for hora in range(1, horas + 1): #de 1 a 12 horas
        while True: #Bucle infinito hasta que se obtenga una entrada válida
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

        # Guardar la cantidad de autos por hora
        horas_concurrencia.append((hora, autos)) #método append agrega un nuevo elemento a la lista. En este caso (hora, autos).

        # Verificar si el estacionamiento estuvo lleno o vacío en algún momento
        if autos == 0:
            horas_vacias.append(hora)
        elif autos == max_autos_por_hora:
            horas_lleno.append(hora)

    # Calcular el promedio de autos
    promedio_autos = total_autos / horas

    # Encontrar las 3 horas con mayor concurrencia
    horas_mas_concurridas = [hora[0] for hora in sorted(horas_concurrencia, key=lambda x: x[1], reverse=True)[:3]] #Toma la lista horas_concurrencia, la ordena por la cantidad de autos en orden descendente y selecciona las tres primeras horas de mayor concurrencia. Luego, crea una nueva lista llamada horas_mas_concurridas que contiene solo las horas de esas tres tuplas.

    # Mostrar resultados
    print("\nResultados:")
    print(f"A) El promedio de autos de la jornada es: {promedio_autos:.0f}") #.0f para que no tenga decimales
    print(f"B) Las 3 horas con mayor concurrencia fueron: {horas_mas_concurridas}")
    
    if horas_vacias:
        print(f"C) El estacionamiento estuvo vacío en las horas: {horas_vacias}")
    else:
        print("C) El estacionamiento no estuvo vacío en ningún momento.")

    if horas_lleno:
        print(f"D) El estacionamiento estuvo lleno en las horas: {horas_lleno}")
    else:
        print("D) El estacionamiento no estuvo lleno en ningún momento.")

# Llamar a la función para ejecutar el programaa
analizar_estacionamiento()
