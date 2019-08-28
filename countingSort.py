import timeit
from random import randint
import matplotlib.pyplot as plt
import sys
from random import shuffle

sys.setrecursionlimit(10 ** 6)


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def countSort(array, maxval):
    m = maxval + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for _ in range(count[a]):
            array[i] = a
            i += 1


size = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = geraLista(s)
    time.append(timeit.timeit("countSort({}, {})".format(lista,max(lista)+1),
                              setup="from __main__ import countSort", number=1))
    print(s)

desenhaGrafico(size, time, "Tamanho", "Tempo",
               "countSort.png")