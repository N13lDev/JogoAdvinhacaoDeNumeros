import random #importa o modulo random
import pygame #Importando a biblioteca pygama
import sys
import time


# ======================= PARTE 1: CONMFIGURAÇÃO BÁSICA =======================

def inicializarPyGame():
    """Inicializa todos os módulos necessários do PyGame"""
    
    pygame.init() #Inicializa o pygame
    pygame.font.init() #Inicializa o sistema de fontes
    pygame.mixer.init() #Inicializa o sistema de áudio

    # RETORNA CONFIGURAÇÕES IMPORTANTES

    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Caçador de Tesouros")
    clock = pygame.time.Clock()

    return tela, clock, largura, altura

def definirCoresFontes():
    """Define as cores e fontes utilizadas no game"""

    # COREES (FORMATO RGB)
    cores = {
        "AZUL_ESCURO": (25, 25, 112),
        "DOURADO": (255, 215, 0),
        "BRANCO": (255, 255, 255),
        "VERMELHO": (255, 0, 0),
        "VERDE": (0, 155, 0),
        "LARANJA": (255, 165, 0),
        "AZUL_CLARO": (135, 206, 250),
        "MARROM": (139, 69, 19),
        "BEGE": (245, 245, 220)
    }

    # FONTES
    fontes = {
        "titulo": pygame.font.SysFont('comicsans', 60),
        "grande": pygame.font.SysFont('comicsans', 36),
        "media": pygame.font.SysFont('comicsans', 28),
        "pequena": pygame.font.SysFont('comicsans', 22)
    }

    return cores, fontes


def inicializarVariaveisGame():
    """Inicializa todas as váriaveis necessárias para o jogo"""
    
    variaveis = {
        "numeroSecreto": random.randint(1,100),
        "Tentativas": 0,
        "maxTentativas": 10,
        "palpite": "",
        "mensagem": "Digite um numero entre 1 e 100!",
        "inputAtivo": True,
        "inputTexto": "",
        "gameOver": False,
        "vitoria": False,
        "dicaTemp": "",
        "tempoDica": 0,
        "historico": [],
        "animacaoFrame": 0,
        "tempoAniomacao": 0,
        "tempoInicio": time.time()
    }

    return variaveis
    

# ======================= PARTE 2: ELEMENTOS VISUAIS =======================


def criarImagensSimples(cores):
    """Cria imagens/superficies simples"""

    imagens = {
        "bau": pygame.Surface((100, 50)),
        "mapa": pygame.surface((200, 150))
    }

    #Preenche as superficies com cores

    imagens["bau"].fill(cores["DOURADO"])
    imagens["MAPA"].fill(cores["MARROM"])

    return imagens


def desenharBotao(tela, x, y, largura, altura, texto, cor, corHover, fonte, corTexto):
    """Desenha um botão interativo na tela
       Retorna True se o botão for clicado
    """

    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    # Verifica se o mouse  está sobre o botão
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(tela, corHover, (x, y, largura, altura), border_radius=10)
        if clique[0] == 1:
            #Aqui poderia ter um som de clique
            return True
    else:
        pygame.draw.rect(tela, cor, (x, y, largura, altura), border_radius=10)

    
    #Texto do botão
    textoSuperficie = fonte.render(texto, True, corTexto)
    textoRect = textoSuperficie.get_rect(center=(x + largura/2, y + altura/2))
    tela.blit(textoSuperficie, textoRect)

    return False


































"""pygame.init() #Prepara o pygame para funcionar

#Configurando a janela
largura, altura = 600, 400 
tela = pygame.display.set_mode((largura, altura)) #Cria uma janela de 600x400 pixels
pygame.display.set_caption("Caçador de Tesouros")
clock = pygame.time.Clock() #Controla a velocidade do jogo(Frames por segundo)

#Variaveis do game
numero_secreto = random.randint(1,100) #Gera um numero entre 1 e 100
tentativas = 0 #Começa com 0 tentativas
palpite = ""
mensagem = "Digite um numero entre 1 e 100!" #Texto inicial na tela
maxTentativas = 10

#print("Bem vindo ao jogo de Advinhação de Números!")
#print("Tente acertar o número entre 0 e 100!")
while tentativas < maxTentativas: #Loop infinito (vamos quebrá-lo depois)
    palpite = int(input("Seu palpite: ")) #Pede o número
    tentativas += 1 #Aumenta o contador de tentativas

    print(f"Voçê tentou {tentativas} vez(es) seu palpite foi {palpite}")

    if abs(palpite - numero_secreto) <= 10: #verifica se está quente
        print("Você está quente!")
    elif abs(palpite - numero_secreto) >= 20:
        print("Você está frio!")

    if palpite == numero_secreto:
        print("=======================================================")
        print(f"Parabéns! Voçê acertou o número secreto {numero_secreto} em {tentativas} tentativa(s)!")
        break  #sai do loop quando acerta
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Muito baixo! Tente novamente.")
if tentativas >= maxTentativas:
    print(f"Game over! O número era {numero_secreto}.")
    print("Boa sorte na próxima!!!")
"""

