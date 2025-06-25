def soma_lista(lista):
    if lista == []:
        return 0
    return lista[0] + soma_lista(lista[1:])

print(soma_lista([1, 2, 3, 4]))