# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

n = 123

# 1 спсоб
res = sum(int(digit) for digit in str(n))
print(res)

# 2 способ
res = 0
for digit in str(n):
    res += int(digit)
print(res)


# 3 способ
print(n//100 + n//10%10 + n%10)

# 4 способ
num = input('Введите 3-х значное число: ')
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print(res)
else:
    print('Вы ввели не 3-х значное число')