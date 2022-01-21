'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
 quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodadEscreva 
 um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele 
 foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodad
'''

dias = float(input("Por quantos dias você utilizou o carro?: "))
km = float(input("Quantos km você rodou com o carro?: "))
resultado_dias = dias * 60
resultado_km = km * 0.15
print("Fazendo os calculos, você rodou {} dias com o carro e rodou {}Km  com o carro, \nentão o preçp as ser pago é R${:.2f} ".format(dias,km,resultado_dias + resultado_km))
