a = int(input('Введите 1-ю сторону: '))
b = int(input('Введите 2-ю сторону: '))
c = int(input('Введите количество долек: '))
if c % a == 0 or c % b == 0:
    print('Yes')
else: print('No')
