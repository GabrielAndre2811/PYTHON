def ordem(lista):
    if len(lista) <= 1:
        return lista
    
    m = lista[0]  # define pivo

    menores = []
    for elemento in lista:
        if elemento < m:
            menores.append(elemento)

    iguais = []
    for elemento in lista:
        if elemento == m:
            iguais.append(elemento)

    maiores = []
    for elemento in lista:
        if elemento > m:
            maiores.append(elemento)

    return ordem(menores) + iguais + ordem(maiores)

# elemento menor que o pivo
# elemento igual ao pivo
# elemento maior que o pivo
# lista = [88, 35, 37, 16, 99, 2, 41]


lista = [88, 35, 37, 16, 99, 2, 41]


print(f"\n Usando recursividade: + {ordem (lista)}")