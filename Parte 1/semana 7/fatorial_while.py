def fatorial(numero):
    fat = 1
    while numero > 1:
        fat = fat * numero
        numero = numero - 1
    return fat


def recebe_usuario():
    numero = int(input("Digite um número:"))
    while numero > -1:
        print(fatorial(numero))
        numero = int(input("Digite um número ou digite 0 para sair:"))


recebe_usuario()
