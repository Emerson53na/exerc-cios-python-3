from math import trunc

n = float(input('Digite um número Decimal: '))
print('O número {} com a sua poção inteira é: \033[32m{}\033[m.'.format(n,trunc(n)))
