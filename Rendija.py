def accion(matriz, vector):
    v = [0 for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] += round(matriz[i][j] * vector[j],2)
    return v
def matrizProbabilidad(rendijas, objetivos):
    dimensiones = rendijas + objetivos + 1 # Se añade una fila para colocar el vector de estado final
    matriz =[[0.0 for j in range(dimensiones)] for i in range(dimensiones)]
    posiciones=[]
    for i in range(dimensiones):
        if (i>=rendijas+1):
            matriz[i][i]=1.0
        if (i>=1 and i<rendijas+1):
            matriz[i][0] = round(1 / rendijas, 3)
    fin,ini= 1,rendijas + 1
    if rendijas%2 == 0: #Numero par de rendijas
        aux1 = (objetivos + 1) //2; aux2 = aux1 - aux1 //2  #Cantidad de objetivos
    elif rendijas%2 == 1:# impar de rendijas
        aux1 = objetivos  // 2; aux2 = aux1 - aux1 // 2 #Cantidad de objetivos
    while ini <= len(matriz) - aux1 and fin < rendijas + 1:
        for i in range(ini+aux1):
            if i>=ini:
                matriz[i][fin] = round(1 / (aux1), 2)
        ini+=aux2
        fin+=1
    return matriz
def escribir(matriz):
    for i in matriz:
        print(i)
def estadoFinal(rendijas, objetivos, repeticiones):
    matriz_Probabilidad = matrizProbabilidad(rendijas, objetivos)
    print("Matriz de probabilidad")
    escribir(matriz_Probabilidad)
    estadoFinal = [1] + [0 for i in range(rendijas + objetivos)]
    for i in range(repeticiones): # Calcula la probabilidad del estado final
        estadoFinal = accion(matriz_Probabilidad,estadoFinal)
    return estadoFinal
