n = int(input("Digite o tamanho da lista: "))
total = 0
for i in range(n):
    
    for j in range(n):
        
        if (i!= j) and ((i+j) % 2 ==0):
            total += i + j
print("Total:", total)