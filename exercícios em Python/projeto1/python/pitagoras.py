'''
Faça um programa que leia o comprimenrto 
do cateto oposto e de um cateto adjacente 
 de um triângulo 
retangulo. calcule e mostre o comprimento 
da hipotenusa
'''
import math
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input("Digite o valor do segundo cateto: "))
hip = math.hypot(c1,c2)
print(hip)