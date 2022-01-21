#Medidor de velocidade
velocidade = float(input('Digite a velocidade encontrada:'))
multa = (velocidade - 80)*7
if velocidade <=80:
    print("Você não levou multa!")
else:
    print('Você ultrapassou então deverá pagar {} '.format(multa))