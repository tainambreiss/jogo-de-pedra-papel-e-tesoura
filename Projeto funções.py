
import random

opçoes_game = ['pedra', 'papel', 'tesoura']
escolha_jogador = int(input('Faça sua escolha: Pedra (1), papel (2) ou tesoura (3).'))
escolha_pc = random.choice(opçoes_game)
print(escolha_pc)

def comparacoes_game(escolha_jogador, escolha_pc):
    if escolha_jogador == 1 and escolha_pc == 'tesoura':
        return "você venceu!"
    elif  escolha_jogador == 1 and escolha_pc == 'papel':
        return "você perdeu!"
    elif  escolha_jogador == 1 and escolha_pc == 'pedra':
        return "empatado!"
    
    if escolha_jogador == 2 and escolha_pc == 'tesoura':
        return "você perdeu!"
    elif  escolha_jogador == 2 and escolha_pc == 'papel':
        return "empatado!"
    elif  escolha_jogador == 2 and escolha_pc == 'pedra':
        return "você venceu!"
    
    if escolha_jogador == 3 and escolha_pc == 'tesoura':
        return "empatado!"
    elif  escolha_jogador == 3 and escolha_pc == 'papel':
        return "você venceu!"
    elif  escolha_jogador == 3 and escolha_pc == 'pedra':
        return "você perdeu!"
    
resultado = comparacoes_game(escolha_jogador, escolha_pc)
print(resultado)

