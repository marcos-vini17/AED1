import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class Main:
    def __init__(self):
        dataset = open('../resultados/insertion_semi.csv', 'r')
        x = []
        y = []
        for line in dataset:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n', ''))
            x.append(valor_x)
            y.append(valor_y)

        dataset.close()
        plt.plot(x, y, label='Semi Ordenados')

        dataset2 = open('../resultados/insertion_desordenado.csv', 'r')
        x = []
        y = []
        for line in dataset2:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n', ''))
            x.append(valor_x)
            y.append(valor_y)

        dataset2.close()
        plt.plot(x, y, label='Desordenados')

        dataset3 = open('../resultados/insertion_ordenado.csv', 'r')
        x = []
        y = []
        for line in dataset3:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n', ''))
            x.append(valor_x)
            y.append(valor_y)

        dataset3.close()
        plt.plot(x, y, label='Ordenados')

        plt.legend()
        plt.grid(True)
        plt.title('Insertion Sort')
        plt.xlabel('Quantidade de entradas')
        plt.ylabel('Tempo (em segundos)')
        plt.show()


Main()
