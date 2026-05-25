import random

def buscar_max_min_mult3(arreglo, inicio, fin):
    if inicio > fin:
        return -1, float('inf') 
        
    if inicio == fin:
        if arreglo[inicio] % 3 == 0:
            return arreglo[inicio], arreglo[inicio]
        else:
            return -1, float('inf')

    mitad = (inicio + fin) // 2

    max_izq, min_izq = buscar_max_min_mult3(arreglo, inicio, mitad)
    max_der, min_der = buscar_max_min_mult3(arreglo, mitad + 1, fin)

    if max_izq > max_der:
        max_final = max_izq
    else:
        max_final = max_der

    if min_izq < min_der:
        min_final = min_izq
    else:
        min_final = min_der

    return max_final, min_final

def calcular_promedio_extremos_mult3(arreglo):
    maximo, minimo = buscar_max_min_mult3(arreglo, 0, len(arreglo) - 1)
    
    if maximo == -1 or minimo == float('inf'):
        print("No se encontraron números multiplos de 3 en el arreglo.")
        return 0
        
    print(f"Maximo multiplo de 3 encontrado: {maximo}")
    print(f"Minimo multiplo de 3 encontrado: {minimo}")
    
    promedio = (maximo + minimo) / 2
    return promedio

def main():
    tamano = int(input("Ingrese el tamaño del arreglo: "))
    while tamano <= 0:
        print("El tamaño debe ser mayor a 0.")
        tamano = int(input("Ingrese el tamaño del arreglo: "))

    arreglo = []
    for i in range(tamano):
        num_aleatorio = random.randint(10, 9999)
        arreglo.append(num_aleatorio)
        
    print("\nArreglo generado:")
    print(arreglo)
    print("-" * 30)

    resultado = calcular_promedio_extremos_mult3(arreglo)
    
    if resultado != 0:
        print(f"El promedio entre el máximo y minimo es: {resultado}")

if __name__ == "__main__":
    main()