'''
crie um programa que meça a velocidade e informe se ouve uta e o valor!
obs: 80 não levou multa 80 + 20 = levou multa grave <80 + 20 levou multa gravissima
'''
velocidade = float(input("Digie a velocidade em que o carro se encontra: "))
if velocidade <= 80:
    print("Você não levou multa!")
elif velocidade > 80 + 10:
    print("Você levou multa leve!")
elif velocidade >= 80 + 20:
    print("você levou multa grave")
elif velocidade > 100:
    print("Você levou multa gravissima")