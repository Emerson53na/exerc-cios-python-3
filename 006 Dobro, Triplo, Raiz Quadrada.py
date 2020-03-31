from os import system

while True:
    system('clear')
    cor={'y':'\033[33m','g':'\033[32m','off':'\033[m'}
    n = int(input('Digite um número:{} '.format(cor['y'])))

    print('{}O dobro de {} vale: {}{}{}.'.format(cor['off'],n,cor['g'],(n*2),cor['off']))
    print('O triplo de {} vale: {}{}{}.'.format(n,cor['g'],(n*3),cor['off']))
    print('A raiz quadrada de {} vale: {}{:.2f}{}.'.format(n,cor['g'],(n**(1/2)),cor['off']))
    opc = str(input('\nDeseja continuar?[S/N] '))

    if opc in 'Nn':
        break
