
#só da certo em lista que os valores estão ordenado, ou ordene os valores antes de puxar esta função
#muito utilizado para listas muito grandes
import random
import time

numeros = list(range(0, 1024)) # cria lista de 0 a 1024

#random.shuffle(numeros) #função para embaralhar lista, voce pode descomentar para testar, vai da sempre falso

antes = time.time()

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista)-1 # numeros de elementos da lista menos 1

    while minimo <= maximo:
        
        meio = (minimo + maximo) // 2 # encontra o elemento do meio
        
        if valor < lista[meio]: # verifica se o valor procurado esta a esquerda ou a direita do meio
            maximo = meio -1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return valor # se o valor for encontrado para aqui
        
    return False # aqui não a valor encontrado


#print(numeros) # printa na tela todos os numeros da lista

busca = executar_busca_binaria(numeros, 400) # aqui você pode alterar o valor para ver se ele existe na lista ou não, 400 existe, 4000 não existe
print(busca)# digite 400 vai da true esta dentro da lista, digite 4000 resulta em false
depois = time.time()

total = (depois - antes) *1000
# a busca é normal mas é uma forma da pesquisa economizar recursos de memoria

if busca >=0:
    print(f"\n Valor:, na posição: {busca}") # vai exibir a posição do elemento e
else:
    print("\nValor não encontrado")

print("\nO tempo gasto para o resultado foi de %0.2f ms" %(total))