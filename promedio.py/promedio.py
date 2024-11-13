def calculate_average(numbers):
    """
    Calcula el promedio de una lista de numeros.
    
    Parametros:
    numbers(list): U7na lista de numeros enteros o flotantes
    
    Retorna:
    float: el promedio de los numeros de la lista

    
    """
    return sum(numbers)/ len(numbers)

print(calculate_average([1,2,3,4,5]))