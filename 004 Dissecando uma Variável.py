cor = {'gren' : '\033[32m', 'red' : '\033[31m', 'off' : '\033[m'}

n = input('Digite algo: ')
print('\nTipo primitivo: {}{}{}'.format(cor['gren'],type(n),cor['off']))

nu = ('{}'.format(n.isnumeric()))
if nu == 'True':
    print('Só tem número: {}{}{}'.format(cor['gren'],nu,cor['off']))
else:
    print('Só tem número: {}{}{}'.format(cor['red'],nu,cor['off']))

ab = ('{}'.format(n.isalpha()))
if ab == 'True':
    print('Só é alfabético: {}{}{}'.format(cor['gren'],ab,cor['off']))
else:
    print('Só é alfabético: {}{}{}'.format(cor['red'],ab,cor['off']))

an = ('{}'.format(n.isalnum()))
if an == 'True':
    print('É alfanumérico: {}{}{}'.format(cor['gren'],an,cor['off']))
else:
    print('É alfanumérico: {}{}{}'.format(cor['red'],an,cor['off']))

up = ('{}'.format(n.isupper()))
if up == 'True':
    print('Só está em maiúsculo: {}{}{}'.format(cor['gren'],up,cor['off']))
else:
    print('Só está em maiúsculo: {}{}{}'.format(cor['red'],up,cor['off']))

lo = ('{}'.format(n.islower()))
if lo == 'True':
    print('Só está em minúsculo: {}{}{}'.format(cor['gren'],lo,cor['off']))
else:
    print('Só está em minúsculo: {}{}{}'.format(cor['red'],lo,cor['off']))

sp = ('{}'.format(n.isspace()))
if sp == 'True':
    print('Só tem espaço: {}{}{}'.format(cor['gren'],sp,cor['off']))
else:
    print('Só tem espaço: {}{}{}'.format(cor['red'],sp,cor['off']))

ti = ('{}'.format(n.istitle()))
if ti == 'True':
    print('É capitalizado: {}{}{}'.format(cor['gren'],ti,cor['off']))
else:
    print('É capitalizado: {}{}{}'.format(cor['red'],ti,cor['off']))
