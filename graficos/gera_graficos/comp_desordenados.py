import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class Main:
    def __init__(self):
        dataset1 = open('../resultados/insertion_desordenado.csv', 'r')
        x = []
        y = []
        for line in dataset1:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n', ''))
            x.append(valor_x)
            y.append(valor_y)

        dataset1.close()

        plt.plot(x, y, label='Insertion Sort')

        dataset2 = open('../resultados/merge_desordenado.csv', 'r')
        x = []
        y = []
        for line in dataset2:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n', ''))
            x.append(valor_x)
            y.append(valor_y)

        dataset2.close()

        plt.plot(x, y, label='Merge Sort')

        dataset3 = open('../resultados/quick_desordenado.csv', 'r')
        x = []
        y = []
        for line in dataset3:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n', ''))
            x.append(valor_x)
            y.append(valor_y)

        dataset3.close()

        plt.plot(x, y, label='Quick Sort')

        plt.legend()
        plt.grid(True)

        plt.title('Comparação: Desordenados')
        plt.xlabel('Quantidade números')
        plt.ylabel('Tempo (em segundos)')

        plt.show()


Main()
