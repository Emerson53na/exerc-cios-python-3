n = float(input('Qual é o salario do funcionário? R$'))
d = n*15/100
print('Um fucionário que ganhava \033[32mR$\033[m{:.2f}, com 15% de aumento, passa a receber \033[32mR${:.2f}\033[m.'.format(n,(n+d)))
