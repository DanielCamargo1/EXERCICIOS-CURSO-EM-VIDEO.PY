"""
àrea de um parede sendo que 1 litro de tinta pinta 2m
"""
la_parede = float(input("informe a largura da parede:"))
h_parede = float(input("Informe a haltura da parede:"))
tamanho_parede = la_parede * h_parede
litros_de_tinta  = tamanho_parede * 2
print('sua parede mede {}m então precisará de {} litros de tinta'.format(tamanho_parede,litros_de_tinta))
