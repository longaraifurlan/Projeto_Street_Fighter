import time

def lutar(jogador, oponente):
    print(f"\n{jogador.nome} VS {oponente.nome}")
    time.sleep(1)

    while jogador.vida > 0 and oponente.vida > 0:
        dano = jogador.atacar()
        defesa = oponente.defender()
        oponente.vida -= dano - defesa
        print(f"\033[32m{jogador.nome} ataca e causa {dano} de dano! Vida de {oponente.nome}: {oponente.vida} / {dano-defesa}\033[m")
        time.sleep(0.5)

        if oponente.vida <= 0:
            break

        dano = oponente.atacar()
        defesa = jogador.defender()
        jogador.vida -= dano - defesa
        print(f"\033[31m{oponente.nome} ataca e causa {dano} de dano! Vida do {jogador.nome}: {jogador.vida} / {dano-defesa}\033[m")
        time.sleep(0.5)

    vencedor = jogador if jogador.vida > 0 else oponente
    print(f"\n🔥 {vencedor.nome} WIN 🔥")
    


