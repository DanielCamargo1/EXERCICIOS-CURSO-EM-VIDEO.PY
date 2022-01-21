# UM programa que diga ou não se sua cidade começa com 'SANTO'
cidade = str(input('Digite o nome da sua cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')
