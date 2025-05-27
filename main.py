from characters.characters_abilit import Ryu, Ken
from utils.combate import lutar

def menu_principal():
    print("=== Street Fighter Python ===")
    print("1. Ryu")
    print("2. Ken")
    escolha = input("Escolha seu personagem: ")

    if escolha == '1':
        jogador = Ryu()
        oponente = Ken()
    else:
        jogador = Ken()
        oponente = Ryu()

    lutar(jogador, oponente)

if __name__ == "__main__":
    menu_principal()
