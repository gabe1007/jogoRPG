from os import *
from random import *

# CLASSE PAI DO JOGO
class personagens:
    def __init__(self, nome, ataque, defesa, saude):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.saude = saude


    def print(self):
        print(f'O personagem {self.nome} possui os seguintes dados:')
        print(f'Ataque.......: {self.ataque}')
        print(f'Defesa.......: {self.defesa}')
        print(f'Saude........: {self.saude}')



# CLASSE PAI DOS INIMIGOS DO JOGO
class inimigos:
    def __init__(self, tipo, ataque, defesa, saude):
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa
        self.saude = saude

    def print(self):
        print(f'{self.tipo} possui os seguintes dados:')
        print(f'Ataque.......: {self.ataque}')
        print(f'Defesa.......: {self.defesa}')
        print(f'Saude........: {self.saude}')
       


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------


# CRIA O PERSONAGEM CAVALEIRO
class cavaleiro(personagens):  # CAVALEIRO HERDA AS CARACTERISTICAS DA CLASSE PAI 'personagens'
    def __init__(self, nome):
        self.ataque = 600
        self.defesa = 400
        self.saude = 500
        super().__init__(nome, self.ataque, self.defesa, self.saude)  # O 'super()' INVOCA OS MÉTODOS DA CLASSE PAI

    def imprimir(self):
        super().print()  # INVOCA A FUNÇÃO 'print' DA CLASSE PAI


# CRIA O PERSONAGEM ARQUEIRO
class arqueiro(personagens):
    def __init__(self, nome):
        self.ataque = 500
        self.defesa = 300
        self.saude = 700
        super().__init__(nome, self.ataque, self.defesa, self.saude)

    def imprimir(self):
        super().print()


# CRIA O PERSONAGEM DA CLASSE MAGO
class mago(personagens):
    def __init__(self, nome):
        self.ataque = 500
        self.defesa = 500
        self.saude = 500
        super().__init__(nome, self.ataque, self.defesa, self.saude)

    def imprimir(self):
        super().print()

# ------------------------------------------------------------------------------------------------------------------------------------


# SEGUNDA CLASSE DE INIMIGOS
class orc(inimigos):
    def __init__(self):
        self.tipo = "Orc"
        self.ataque = 500
        self.defesa = 550
        self.saude = 450
        super().__init__(self.tipo, self.ataque, self.defesa, self.saude)

    def imprimir(self):
        super().print()


# TERCEIRA CLASSE DE INIMIGOS 
class oruk(inimigos):
    def __init__(self):
        self.tipo = "Oruk"
        self.ataque = 500
        self.defesa = 500
        self.saude = 500
        super().__init__(self.tipo, self.ataque, self.defesa, self.saude)

    def imprimir(self):
        super().print()

# ---------------------------------------------------------------------------------------------------------------------------------

# FUNÇÃO MOSTRA AS INSTRUÇÕES DO JOGO
def instrucoes():

    print('*****************************  TALVEZ VOCÊ SOBREVIVA  ****************************************\n')
    print('INSTRUÇÕES:')
    print('1 - Escolha um personagem. pode ser um cavaleiro, arqueiro ou mago')
    print('2 - Após escolher o personagem, de um nome ao guerreiro')
    print('3 - Tente sobreviver aos ataques dos inimigos')
    system('pause')
    system('cls')


# FUNÇÃO REFERENTE AO MENU DE OPÇÕES DISPONIVEIS AO USUÁRIO 
def menu():

    escolha = 0
    lista = [1,2,3]

    while escolha not in lista:
        try:
            escolha = int(input('Escolha entre:\n 1) Cavaleiro\n 2) Arqueiro\n 3) Mago\n'))
        except:
            print('Opção inválida, tente novamente')

    return escolha
    

# FUNÇÃO CRIA UM PERSONAGEM 
def criarPersonagem(opcao):

    if opcao == 1:
        nome = input('Digite o nome do personagem: ')
        system('cls')
        character = cavaleiro(nome)
        character.print()

    elif opcao == 2:
        nome = input('Digite o nome do personagem: ')
        system('cls')
        character = arqueiro(nome)
        character.print()
    
    elif opcao == 3:
        nome = input('Digite o nome do personagem: ')
        system('cls')
        character = mago(nome)
        character.print()
    
    else:
        print('Opção inválida. TENTE NOVAMENTE')

    return character


# Função escolhe o inimigo que será selecionado 
def selecionaInimigo():

    escolha = randrange(1, 3)

    if escolha == 1:
        inimigo = orc()
        return inimigo
        
    else:
        inimigo = oruk()
        return inimigo


# Realiza o ataque, sorteando um valor, se for um o ataque acontece, se for 2 o inimigo desvia do ataque 
def ataque(foe, personagem):
    sortearAtaque = randrange(1, 3)
    system('cls')
    var = personagem.saude - 25 # Para cada ataque, são reduzido 25 de saúde 
    personagem.saude = var

    if sortearAtaque == 1:
        print('Você acertou o ataque')
        saude = foe.saude - (personagem.ataque - foe.defesa)
        foe.saude = saude
        
    else:
        print(f'O {foe.tipo} desviou do ataque')        
        
    return foe, personagem
    

# O inimigo realiza o ataque
def ataqueInimigo(foe, personagem):
    sortearAtaque = randrange(1, 3)
    var = foe.saude - 25 # Para cada ataque, são reduzido 25 de saúde 
    foe.saude = var

    if sortearAtaque == 1:
        print('O inimigo acertou o ataque')
        saude = personagem.saude - (foe.ataque - personagem.defesa)
        personagem.saude = saude
        
    else:
        print(f'{personagem.nome} desviou do ataque')        
        
    return foe, personagem
    

# Função serve para iniciar uma nova partida
def jogarNovamente():
    escolha = 0
    opcoes = [1, 2] 

    escolha = int(input('Deseja jogar novamente? 1 - SIM   2 - NÃO\n'))

    if escolha == 1:
        opcao = menu()
        personagem = criarPersonagem(opcao)
        jogar(personagem)

    
# FUNÇÃO ONDE A DIVERSÃO COMEÇA
def jogar(personagem):
    escolha = 0
    lista = [1,2]

    system('pause')
    system('cls')
    print('Agora que o personagem está criado, você está preparado para a batalha?')
    print('Pergunta retórica, agora não tem volta\nSe prepara bonitão, o bicho vai pegar\n')

    # A função 'selecionaInimigo' é chamada mais de uma vez para que mais de um inimigo possa ser selecionado
    foe = selecionaInimigo()
    print(f'O seu inimigo é do tipo {foe.tipo}\n')    
    
    while escolha not in lista: # criar uma função separada para este bloco, para retornar somente a escolha 
        try:
            escolha = int(input('Pressione 1 para atacar ou 2 para fugir: '))
            if escolha == 1:
                while escolha == 1:
                    foe, personagem = ataque(foe, personagem)
                    print(foe.print())
                    system('pause')
                    system('cls')

                    # Este if checa se houve um ganhador
                    if foe.saude <= 0:
                        print('Parabéns, você ganhou o jogo')
                        jogarNovamente()

                    print(f'Agora é a vez do {foe.tipo} atacar. Se prepare!!!')
                    foe, personagem = ataqueInimigo(foe, personagem)
                    print(personagem.print())
                    system('pause')
                    system('cls')
                    
                    # Este if checa se houve um ganhador
                    if personagem.saude <= 0:
                        print('GAME OVER BONITÃO')
                        jogarNovamente()

                    escolha = int(input('Pressione 1 para atacar ou 2 para fugir: '))
                else:
                    print('Covarde')
                              
            elif escolha == 2:
                print('COVARDE')
        except:
            print('Opção inválida, tente novamente')



# main
instrucoes()
opcao = menu()
personagem = criarPersonagem(opcao)
jogar(personagem)



    
