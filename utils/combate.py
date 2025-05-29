import time

def lutar(jogador, oponente):
    print(f"\n{jogador.nome} VS {oponente.nome}")
    time.sleep(1)

    while jogador.vida > 0 and oponente.vida > 0:
        dano = jogador.atacar()
        oponente.vida -= dano
        print(f"{jogador.nome} ataca e causa {dano} de dano! Vida do {oponente.nome}: {oponente.vida}")
        time.sleep(1)

        if oponente.vida <= 0:
            break

        dano = oponente.atacar()
        jogador.vida -= dano
        print(f"{oponente.nome} ataca e causa {dano} de dano! Vida do {jogador.nome}: {jogador.vida}")
        time.sleep(1)

    vencedor = jogador if jogador.vida > 0 else oponente
    print(f"\n🔥 {vencedor.nome} venceu a luta! 🔥")


