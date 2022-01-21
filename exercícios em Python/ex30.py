#Par ou impar
num = int(input("Digite um valor inteiro: "))
resto = num % 2
if resto == 0:
    print("O número {} é par ".format(num))
else:
    print("O númeo {} é ímpar".format(num))