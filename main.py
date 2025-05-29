from characters.characters_abilit import Ryu, Ken, Blanka, ChunLi, EHonda, Guile, Dhalsim, Zangief, MBison
from utils.combate import lutar

# Dicionário com os personagens disponíveis
personagens = {
    '1': Ryu,
    '2': Ken,
    '3': Blanka,
    '4': ChunLi,
    '5': EHonda,
    '6': Guile,
    '7': Dhalsim,
    '8': Zangief,
    '9': MBison

}

def mostrar_menu():
    print("=== Street Fighter Python ===")
    for codigo, personagem in personagens.items():
        print(f"{codigo}. {personagem().__class__.__name__}")

def escolher_personagem(tipo):
    while True:
        escolha = input(f"Escolha o {tipo}: ")
        if escolha in personagens:
            return personagens[escolha]()
        print("Opção inválida. Tente novamente.")

def menu_principal():
    mostrar_menu()
    jogador = escolher_personagem("seu personagem")
    oponente = escolher_personagem("oponente")

    if jogador.nome == oponente.nome:
        print("\n⚠️ Os personagens não podem ser iguais. Escolha o oponente novamente.\n")
        return menu_principal()

    lutar(jogador, oponente)

if __name__ == "__main__":
    menu_principal()
