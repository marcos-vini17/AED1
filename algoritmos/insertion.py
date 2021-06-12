import time
from dados import *

# variável global para contar o número de comparações
comp = 0


def insertionsort(v):
    global comp
    i = 1
    while i < len(v):
        aux = v[i]
        troca = False
        j = i - 1
        while j >= 0 and v[j] > aux:
            v[j + 1] = v[j]
            troca = True
            j -= 1
            comp += 1
        if troca:
            v[j + 1] = aux
        i += 1


# Executando algoritmo Insertion Sort
tipo = input("Digite o tipo de arquivo que vc quer ordenar:\n1 - Ordenado\n2 - Desordenado\n3 - Semiordenado\n ")
vetor = None
if tipo == '1':
    vetor = ordenado()
elif tipo == '2':
    vetor = desordenado()
elif tipo == '3':
    vetor = semiordenado()
else:
    print("Opção inválida!")

print("\nINSERTIONSORT")
print("O arquivo inicial é:", end=" ")
print(vetor)

tI = time.time()
insertionsort(vetor)
tF = time.time()

tempo = (tF - tI)

print("O arquivo ordenado é:", end=" ")
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {tempo} s')
