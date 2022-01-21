'''
 • Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
print("-="*21)
print("Calxuladodra de IMC")
print("-="*21)
p = float(input('Digite o seu peso: '))
h = float(input('Digite o sua altura: '))
imc = p / (h**2)
if imc < 18.5:
    print('Seu IMC é {:.2f} '.format(imc))
    print('ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f} '.format(imc))
    print("PESO IDEAL")
elif 25 < imc <= 30:
    print('SOBREPESO')
    print('Seu IMC é {:.2f} '.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f} '.format(imc))
    print('OBESIDADE')
else:
    print('Seu IMC é {:.2f} '.format(imc))
    print('OBESIDADE MÓRBIDA')
