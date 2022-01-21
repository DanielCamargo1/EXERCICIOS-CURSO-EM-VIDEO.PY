'''
Crie um programa que mostre quanto uma pessoa tem na carteira e em seguida
mostre quatos dolares ela pode comprar
'''
carteira = float(input("Com qual valor você deseja comprar: R$ "))
converçao = carteira / 3.27
print('Você consegue comprar: US${:.2f}'.format(converçao))