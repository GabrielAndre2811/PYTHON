#fatorial iterative
def fatorial_iterativo(n):
    resultado = 1 # inicializa o resultado como 1
    n = n + 1 # para incluir o número n no fatorial
    for i in range(2, n):#5 numeros
        resultado *= i
    return resultado

print(f"Fatorial iterativo de 5: {fatorial_iterativo(4)}") # 120

