def heap_sort(data):
    tamanho = len(data)
    indice = int(tamanho/2)
    pai = 0
    filho = 0
    temp = 0
    while True:
        if indice > 0:
            indice -= 1
            temp = data[indice]
        else:
            tamanho -= 1
            if tamanho == 0:
                return
            temp = data[tamanho]
            data[tamanho] = data[0]
        pai = indice
        filho = indice * 2 + 1
        while filho < tamanho:
            if (filho + 1) < tamanho and data[filho+1] > data[filho]:
                filho += 1
            if data[filho] > temp:
                data[pai] = data[filho]
                pai = filho
                filho = pai * 2 + 1
            else:
                break
        data[pai] = temp


lista = []
for i in range(10, 0, -1):
    lista.append(i)

heap_sort(lista)

print(lista)
