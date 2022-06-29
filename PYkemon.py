import random

stab = None
class Pokemon():
    def __init__(self,nome, tipo, atk, defesa, hp, speed):
        self.nome = nome
        self.tipo = tipo
        self.atk = atk
        self.defesa = defesa
        self.hp = hp
        self.speed = speed
    def printar(self):
        print(f"Seu {self.nome} possuí {self.hp} de vida")


class ataques():
    def __init__(self, nome , pp, dano, tipo):
        self.pp = pp
        self.dano = dano
        self.tipo = tipo       

Squirtle = Pokemon("Squirtle", "water", 48, 65, 44, 39)

Charmander = Pokemon("Charmander", "fire", 52, 43, 39, 45)

Bulbasauro = Pokemon("Bulbasaur", "grass",49, 49, 45, 60)

bubble = ataques("bubbles", 30, 40, "water")
ember = ataques("ember", 30, 40, "fire")
vine_whip = ataques("vine_whip", 30, 40, "grass")

poke = [Squirtle, Bulbasauro]
ataquesdooponente = [bubble, ember, vine_whip]

def escolherpoke():
    escolha = int(input("""Qual sua escolha?
    1 - Squirtle
    2 - Bulbasauro
    3 - Charmander"""))

    if escolha == 1:
        return Squirtle
    elif escolha == 2:
        return Bulbasauro
    elif escolha == 3:
        return Charmander
    
suaescolha = escolherpoke()


def escolhaoponente():
    return random.choice(poke)

escolhadoponente = escolhaoponente()



    


def calculardano(poke1, poke2, ataque):
        
    return(((((2*10/5+2)*poke1.atk*ataque.dano/poke2.defesa)/50)+2)*1.5*1*(80/100) // 1)

def calculardanooponente(poke1, poke2, ataque):

    return(((((2*10/5+2)*poke2.atk*ataque.dano/poke1.defesa)/50)+2)*1.5*1*(80/100) // 1)

def escolherataque():
    escolha = int(input(f"""Qual ataque seu {suaescolha.nome} vai usar?
    1 - Para Bubbles
    2 - Para Ember
    3 - Para Vine Whip"""))

    if escolha == 1:
        return bubble
    elif escolha == 2:
        return ember
    elif escolha == 3:
        return vine_whip
def ataqueoponente():
    return random.choice(ataquesdooponente)

def mostrardano(poke1, poke2, ataque):
    print(f""" {"=" * 25 }
    O {poke2.nome} do seu oponente tomou {calculardano(poke1, poke2, ataque)} de dano
    {"=" * 25 } """)
    poke2.hp -= calculardano(poke1, poke2, ataque)
    print(f"""{"=" * 25 }
     Agora a vida do {poke2.nome} do seu oponente é de : {poke2.hp}
     {"=" * 25 }""")

def mostrardanooponente(poke1, poke2, ataque):
    print(f"""{"=" * 25 }
    O seu {poke1.nome} tomou {calculardano(poke1, poke2, ataque)} de dano
    {"=" * 25 } """)
    poke1.hp -= calculardano(poke1, poke2, ataque)
    print(f"""{"=" * 25 }
     Agora a vida do seu {poke1.nome} é de : {poke1.hp}
     {"=" * 25 }""")






def vervida():
    if Charmander.hp <= 0 or Bulbasauro.hp <= 0 or Squirtle.hp <= 0:
        return False
    else:
        return True 

while vervida() == True:
    ataquedooponente = ataqueoponente()
    seuataque = escolherataque()
    
    mostrardano(suaescolha, escolhadoponente, seuataque)
    vervida()

    mostrardanooponente(suaescolha, escolhadoponente, seuataque)
    vervida()





