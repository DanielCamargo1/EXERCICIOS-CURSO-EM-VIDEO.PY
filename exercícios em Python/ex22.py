#Crie um programa onde leia o nome de uma pessoa e mostre:
# 1 - toda as letras maiusculas
# 2 - O nome com todas minusculas
# 3 - Quantas letras ao todo, sem considerar os esspaços
# 4 - qunatas lerras em o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print("Analisando o seu nome...")
print("Em letras maiusculas:{} ".format(nome.upper()))
print("Em letras minusculas: {} ".format(nome.lower()))
print("A qunatidade de letras são {} ".format(len(nome) - nome.count(' ')))
#print("Quantas letras possui o seu primeiro noe:{} ".format(nome.find(" ")))
f_name = nome.split()
print("O seu primeiro nome é {} e ele possui {} letras ".format(f_name[0],len(f_name[0])))


