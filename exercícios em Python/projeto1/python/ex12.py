'''
Deu a louca no gerente!!!!!
uma loja esta com um preço de liquidação, exiba um valor de 5% de desconto
'''
preco = float(input("Adcione um valor: "))
li = preco - (preco * 5 / 100)
print("De inicio o valor era {} com o descpnto passou a ser {}".format(preco,li))