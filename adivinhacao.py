# importação da biblioteca
import random
# sorteio do número aleatório
numero = random.randint(0,10)
# TESTE
#print(numero)
tentativas = 1
while (tentativas <= 3):
    print("Tentativa:", tentativas)
    chute = int(input("Digite o seu chute (0 a 10):"))
    if chute == numero:
        print("Parabéns, você é o bonzão mesmo")
        break
    else:
        print("Errou :c")
    tentativas = tentativas + 1
print("### FIM DO JOGO ###")
# Exercício: caso a pessoa erre todas as tentativas,
# mostre o número sorteado ao final do jogo