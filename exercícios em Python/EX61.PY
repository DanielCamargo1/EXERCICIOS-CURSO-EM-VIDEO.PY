print('=========== GERADOR DE PA     ==========')
primeiro = int(input('Digite um valor: '))
razão = int(input('Digite a razão: '))
cont = 1
termo = primeiro
while cont <=10:
    print(' {} '.format(termo), end='')
    termo = termo + razão
    cont += 1
print('FIM')



