def somar_numero(numero):
    if numero == 1:
        return 1
    else:
        return numero + somar_numero(numero -1)

print(somar_numero(3))