def deszyfr(alfabet, lista):
    l = [0] * len(lista)
    for i in range(len(lista)):
        if lista[i][0] == 0:
            l[lista[i][1] // 10 - 1] = ' '
        else:
            l[lista[i][1] // 10 - 1] = alfabet[lista[i][0] // 10 - 1]
    return ''.join(l)


