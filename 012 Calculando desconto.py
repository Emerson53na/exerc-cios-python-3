n = float(input('Qual é o preço do produto? R$'))
d = n*5/100
print('O produto que custava R${:.2f} na promoção com desconto de 5% vai custar \033[32mR${:.2f}\033[m.'.format(n,(n-d)))
