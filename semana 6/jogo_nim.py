def computador_escolhe_jogada(n, m):
    count = 0
    while n % (m + 1) != 0:
        count += 1
        n -= 1
    if count == 0:
        return m
    elif 0 < count <= m:
        a_remover = n - (n - count)
        return a_remover
    else:
        return m


def usuario_escolhe_jogada(n, m):
    if n <= m:
        m = n
    a_remover = 0
    a_remover = int(input("Quantas peças você vai tirar? "))
    while a_remover > m or a_remover < 1:
        print("Oops! Jogada inválida! Tente de novo.")
        a_remover = int(input())
    return a_remover


def partida():
    n = -1
    m = -1
    while n <= m:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada?: "))
    vez_pc = 0
    vez_jogador = 0
    vencedor = 0
    if n % (m + 1) == 0:
        print("Você começa!")
        a_remover = usuario_escolhe_jogada(n, m)
        print("Você tirou", a_remover, "peças")
        n = n - a_remover
        print("Agora restam", n, "peças no tabuleiro")
        vez_jogador += 1
    else:
        print("Computador começa!")
        a_remover = computador_escolhe_jogada(n, m)
        print("O computador tirou", a_remover, "peças")
        n = n - a_remover
        print("Agora restam", n, "peças no tabuleiro")
        vez_pc += 1
    while n > 0:
        if vez_pc < vez_jogador:
            a_remover = computador_escolhe_jogada(n, m)
            print("O computador tirou", a_remover, "peças")
            n = n - a_remover
            print("Agora restam", n, "peças no tabuleiro")
            vez_pc += 2
            if n == 0:
                vencedor = 1
        else:
            a_remover = usuario_escolhe_jogada(n, m)
            print("Você tirou", a_remover, "peças")
            n = n - a_remover
            print("Agora restam", n, "peças no tabuleiro")
            vez_jogador += 2
            if n == 0:
                vencedor = 2
    if vencedor == 1:
        print("Fim do jogo! O computador ganhou!")
        computador = 1
        return "computador"
    else:
        print("Fim do jogo! você ganhou!")
        return "jogador"


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    resposta = input()
    jogador = 0
    computador = 0
    i = 1
    if resposta == "1":
        partida()
    else:
        print("Voce escolheu um campeonato!")
        while i <= 3:
            print("**** Rodada", i, "****")
            a = partida()
            if a == "jogador":
                jogador += 1
            else:
                computador += 1
            i += 1
        print("**** Final do campeonato! ****")
        print("Placar: Você", jogador, "X", computador, "Computador")


main()
