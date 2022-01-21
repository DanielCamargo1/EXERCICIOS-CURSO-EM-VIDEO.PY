'''import math
print("Ângulos disponiveis: 30, 45, 60.")
ang = int(input("Digite um angulo desejado: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print("O seno de {} é {:.2f} ".format(ang,sen))
print('O cosseno de {} é {:.2f}'.format(ang,cos))
print('A tangente do anngulo {} é {:.2f}'.format(ang,tg))'''

import math
print("-="*21)
print("Os ângulos disponiveis sâo: 30, 45, 60")
print("-="*21)
ang_des = int(input("Digite o ângulo que você deseja: "))
print("-="*21)
sen = math.sin(math.radians(ang_des))
cos = math.cos(math.radians(ang_des))
tg =  math.tan(math.radians(ang_des))
if ang_des == 30:
    print("""Opções disponiveis:
    [ 1 ] SENO
    [ 2 ] COSSENO
    [ 3 ] TANGENTE """)
    opc = int(input('digite a opção disponivel: '))
    if opc == 1:
        print('O seno de {} é {:.2f} '.format(ang_des,sen))
    elif opc == 2:
        print('O cosseno de {} é {:.2f} '.format(ang_des,cos))
    elif opc == 3:
        print('A Tangente de {} é {:.2f} '.format(ang_des,tg))
elif ang_des == 45:
    print("""Opções disponiveis:
    [ 1 ] SENO
    [ 2 ] COSSENO
    [ 3 ] TANGENTE """)
    opc = int(input('digite a opção disponivel: '))
    if opc == 1:
        print('O seno de {} é {:.2f} '.format(ang_des,sen))
    elif opc == 2:
        print('O cosseno de {} é {:.2f} '.format(ang_des,cos))
    elif opc == 3:
        print('A Tangente de {} é {:.2f} '.format(ang_des,tg))
    else:
        print('Por  favovr digite um número que corrsponde!')
elif ang_des == 60:
     print("""Opções disponiveis:
    [ 1 ] SENO
    [ 2 ] COSSENO
    [ 3 ] TANGENTE """)
     opc = int(input('digite a opção disponivel: '))
     if opc == 1:
        print('O seno de {} é {:.2f} '.format(ang_des,sen))
     elif opc == 2:
        print('O cosseno de {} é {:.2f} '.format(ang_des,cos))
     elif opc == 3:
         print('A Tangente de {} é {:.2f} '.format(ang_des,tg))