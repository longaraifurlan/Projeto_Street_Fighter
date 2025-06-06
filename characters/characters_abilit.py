import random

class Personagem:
    def __init__(self, nome, vida, forca, defesa):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa

    def atacar(self):
        return self.forca

    def defender(self):
        return self.defesa


class Ryu(Personagem):
    def __init__(self):
        super().__init__("Ryu", 100, 15, 8)

    def atacar(self):
        variacao_atac = random.randint(-5, 1)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
#----------------------------------------------------

class Ken(Personagem):
    def __init__(self):
        super().__init__("Ken", 100, 14, 7)
    
    def atacar(self):
        variacao_atac = random.randint(-6, 2)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
#----------------------------------------------------

class Guile(Personagem):
    def __init__(self):
        super().__init__("Guile", 100, 9, 9)
    
    def atacar(self):
        variacao_atac = random.randint(-1, 4)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
#---------------------------------------------------

class ChunLi(Personagem):
    def __init__(self):
        super().__init__("Chun-Li", 100, 9, 8)
    
    def atacar(self):
        variacao_atac = random.randint(-2, 5)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
#--------------------------------------------------

class EHonda(Personagem):
    def __init__(self):
        super().__init__("E.Honda", 100, 8, 8)
    
    def atacar(self):
        variacao_atac = random.randint(-4, 8)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
#--------------------------------------------------

class Blanka(Personagem):
    def __init__(self):
        super().__init__("Blanka", 100, 9, 10)

    def atacar(self):
        variacao_atac = random.randint(-1, 3)
        return max(self.forca + variacao_atac, 0)

    def defender(self):
        print(f"{self.nome} solta uma descarga elétrica ao defender!⚡")
        return self.defesa + 1
#--------------------------------------------------

class Dhalsim(Personagem):
    def __init__(self):
        super().__init__("Dhalsim", 100, 8, 9)
    
    def atacar(self):
        variacao_atac = random.randint(-1, 3)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
#--------------------------------------------------

class MBison(Personagem):
    def __init__(self):
        super().__init__("M.Bison ", 105, 12, 9)
    
    def atacar(self):
        variacao_atac = random.randint(-4, 4)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
#-------------------------------------------------

class Zangief(Personagem):
    def __init__(self):
        super().__init__("Zangief", 100, 8, 9)
    
    def atacar(self):
        variacao_atac = random.randint(-1, 3)
        return max(self.forca + variacao_atac, 0)
    
    def defender(self):
        variacao_def = random.randint(-2, 2)
        return max(self.defesa + variacao_def, 0)
