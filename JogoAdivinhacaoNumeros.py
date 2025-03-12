import random #importa o modulo random

numero_secreto = random.randint(1,100) #gera um numero entre 1 e 100
tentativas = 0 #começa com 0 tentativas
maxTentativas = 10

print("Bem vindo ao jogo de Advinhação de Números!")
print("Tente acertar o número entre 0 e 100!")
while tentativas < maxTentativas: #loop infinito (vamos quebrá-lo depois)
    palpite = int(input("Seu palpite: ")) #pede o número
    tentativas += 1 #aumenta o contador de tentativas

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
Próximos Passos
Tente adicionar um placar para várias rodadas (use uma lista para salvar tentativas).

Transforme em um jogo gráfico com pygame (ex.: mostre o número de tentativas na tela).

Flexibilidade: Você pode ajustar o "10" para mudar a dificuldade.

Mostrar a distância: Substitua por print(f"Distância: {abs(palpite - numero_secreto)}") para debug ou como dica opcional

"""
