
# ANALSIS EJERCICIO

# PRIMERA IMPRESION

# Se detecta que es una función que ordena una lista y que solicita un input_list como parametro.

# Funcion original

def sort_list(input_list):
    print("Lista de entrada:", input_list)
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j] = input_list[j + 1], input_list[j]  # El error 
    print("Lista ordenada:", input_list)
    return input_list

# Error en codigo original

# El error en la función original de arriba se encunetra en la linea 15, ya que se intenta asignar 
# dos veces input_list[j], algo que es redundante y hace que la funcion no funcione correctamente.


#Funcion Mejorada
 
def sort_list(input_list):
    print("Lista de entrada:", input_list)
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    print("Lista ordenada:", input_list)
    return input_list

# Solución en codigo original

# El error ya se arregló, ahora ya se asignan los valores despues del if de manera adecuada y la
# funcion si cumple su objetivo de ordenar 


# Se llama la funcion
sort_list([5, 6, 9, 7, 1, 10])

