# importação da biblioteca
import random

# Configurações do jogo
tentativas = 1
errou = True
sorteio_max = 10
tentativas_max = 3
numero = random.randint(0,sorteio_max)


while (tentativas <= tentativas_max):
    print("Tentativa:", tentativas)
    chute = int(input("Digite o seu chute (0 a 10):"))
    if chute == numero:
        print("Parabéns, você é o bonzão mesmo")
        errou = False
        break
    else:
        print("Errou :c")
    tentativas = tentativas + 1
    
if errou == True:
    print("O número sorteado era:", numero) # mostra p quem errou
print("### FIM DO JOGO ###")
