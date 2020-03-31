n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

nw = (n1/2)+(n2/2)
if nw == 6:
    print('A média entre {} e {} é: \033[32m{:.1f}\033[m.'.format(n1,n2,nw))
elif nw == 5:
    print('A média entre {} e {} é: \033[33m{:.1f}\033[m.'.format(n1,n2,nw))
else:
    print('A média entre {} e {} é: \033[31m{:.1f}\033[m.'.format(n1,n2,nw))
