numero = int(input("Digite um valor inteiro de 1 a 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("A unidade é: {} ".format(u))
print('A dezena de {} '.format(d))
print('A centena de {} '.format(c))
print('O milhar {} '.format(m))