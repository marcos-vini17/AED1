import time
from dados import *

comp = 0


def mergesort(vetor, pI, pF):
    if pI < pF:  # condição de existência
        q = (pI + pF) // 2  # meio do vetor
        mergesort(vetor, pI, q)  # cria um subvetor que é a metade a esquerda do vetor anterior
        mergesort(vetor, q + 1, pF)  # cria um subvetor que é a metade a direita do vetor anterior
        intercalar(vetor, pI, q, pF)


def intercalar(vetor, pI, q, pF):
    global comp
    vetorCopia = vetor.copy()  # Cópia do vetor real
    contE = pI  # Contador do subvetor a esquerda
    contD = q + 1  # Contador do subvetor a direita
    contR = pI  # Contador do vetor real

    while contR <= pF:
        comp += 1
        # Entra quando não existe mais elementos no subvetor a esquerda
        if contE > q:
            vetor[contR] = vetorCopia[contD]
            contD += 1
        # Entra quando não existe mais elementos no subvetor a direita
        elif contD > pF:
            vetor[contR] = vetorCopia[contE]
        # Troca elemento do subvetor a esquerda
        elif vetorCopia[contE] <= vetorCopia[contD]:
            vetor[contR] = vetorCopia[contE]
            contE += 1
        # Troca elemento do subvetor a direita
        else:
            vetor[contR] = vetorCopia[contD]
            contD += 1
        contR += 1


# Executando algoritmo Merge Sort
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

print("\nMERGESORT")
print("O vetor inicial é:", end=" ")
print(vetor)

tI = time.time()
mergesort(vetor, 0, len(vetor) - 1)
tF = time.time()

tempo = (tF - tI)

print("O vetor ordenado é:", end=" ")
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {tempo} s')
