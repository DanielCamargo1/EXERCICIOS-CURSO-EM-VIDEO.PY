'''
crie um programa que calcule o valor de uma passegem 
de uma viagem por km. ConsiderNDO 0,50 POR KM para 
viagens até 200 km e 0,45 para viagens mais longas
'''
distancia = float(input('Digite a distancia em KM da viagem: '))
if distancia <= 200:
    preço = distancia * 0,50
else:
    preço = distancia * 0,45
print('O valor que você deverá pagar é de {:.2f } '.format(preço))


