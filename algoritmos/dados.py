def ordenado():
    arquivo = input("Digite o tamanho do arquivo: ")
    text_file = open(f"gera_dados/ordenado/ordenado{arquivo}.dat", "r")
    lines = text_file.readlines()
    text_file.close()
    return lines


def semiordenado():
    arquivo = input("Digite o tamanho do arquivo: ")
    text_file = open(f"gera_dados/semiordenado/semiordenado{arquivo}.dat", "r")
    lines = text_file.readlines()
    text_file.close()
    return lines


def desordenado():
    arquivo = input("Digite o tamanho do arquivo: ")
    text_file = open(f"gera_dados/desordenado/desordenado{arquivo}.dat", "r")
    lines = text_file.readlines()
    text_file.close()
    return lines
