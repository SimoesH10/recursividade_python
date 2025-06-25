def contar_elementos(lista):
    if lista == []:
        return 0
    return 1 + contar_elementos(lista[1:])


print(contar_elementos([1, 2, 3, 4])) 