'''
 • Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0  termos.
'''
print('=========== DERADOR DE PA ==========')
primeiro = int(input('Digite um valor: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
des = 10
while des != 0:
    total += des
    while cont <= total:
        print(' {} '.format(termo), end='')
        termo = termo + razão
        cont += 1
    des = int(input('deseja ver quantos números? :  '))
    
print('Progresso finalizado com {} termos gerados'.format(total))