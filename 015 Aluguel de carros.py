dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (dia * 60) + (km * 0.15)
print('O total a pagar é de \033[32mR${:.2f}\033[m.'.format(valor))
