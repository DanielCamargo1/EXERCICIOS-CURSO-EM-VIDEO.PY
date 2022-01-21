'''
um valor em metros e exiba qnts cm e mm
input adicione um valor em metros
cm = metros / 100
mm = metros / 1000
print o valo em cm é {} o valor em mm é{}
'''
metros = int(input("Adicione um valor em metros: "))
cm = metros / 100
mm = metros / 1000
print("O valor em centimetros é {} o valor em milímetros é {}".format(cm,mm))