import time
from dados import *

# variável global para contar o número de comparações
comp = 0


def quicksort(vetor, pI, pF):
    if pI < pF:  # Condição de existência
        pF_pivo = particionar(vetor, pI, pF)
        quicksort(vetor, pI, pF_pivo - 1)  # Ordenar os elementos menores que o pivô
        quicksort(vetor, pF_pivo + 1, pF)  # Ordenar os elementos maiores que o pivô


def particionar(vetor, pI, pF):
    global comp
    pivo = vetor[pI]  # O primeiro elemento do vetor
    destino = pI  # Destino do pivô, inicializado no local onde o pivo está
    i = pI + 1  # Parâmetro para percorrer o restante do vetor
    while i <= pF:
        comp += 1
        if vetor[i] < pivo:  # Verifica se o elemento iterado é menor do que o pivo
            destino += 1  # Incrementa a posição de destino
            trocar(vetor, destino, i)
        i += 1  # Passa próximo elemento

    trocar(vetor, pI, destino)
    return destino


def trocar(vetor, e1, e2):
    aux = vetor[e1]
    vetor[e1] = vetor[e2]
    vetor[e2] = aux


# Executando algoritmo Quick Sort
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

print("\nQUICKSORT")
print('O vetor inicial é: ', end='')
print(vetor)

tI = time.time()
quicksort(vetor, 0, len(vetor) - 1)
tF = time.time()

tempo = (tF - tI)

print(f'O vetor ordenado é: ', end='')
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {tempo} s')
