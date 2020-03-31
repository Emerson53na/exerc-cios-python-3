m = float(input('Digite a distância em metros: '))
print('A medida {}m corresponde a\n\033[32m{}km\n{}hm\n{}dam'.format(m,(m/1000),(m/100),(m/10)))
print('{}dm\n{}cm\n{}mm\033[m'.format((m*10),(m*100),(m*1000)))
