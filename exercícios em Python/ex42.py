'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
print("-="*21)
print("analisador de triângulos")
print("-="*21)
a = float(input('Digite o valor de um lado: '))
b = float(input('digite o valor deoutro lado: '))
c = float(input('Digite o valor do ultimo lado: '))
if a < b + c and b < a + c and c < a + b:
    print("Esses volores correspondem, então PODE SER UM TRIÂNGULO!!", end='')
    if a == b ==c:
        print("O triângulo é EQUILATERO!")
    elif a != b != c != a:
        print('Esses triangulo é ESCALENO!!!')
    else:
        print('ISÓCELES')
else:
    print('Não pode formar triangulo!')