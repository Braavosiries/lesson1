max_1 = 0
n1 = 0
n = int(input('Введите положительное целое число: '))
while n > 0:
    n1 = n % 10
    n = n // 10
    if n1 > max_1:
        max_1 = n1
    else:
        max_1 = max_1

print(max_1)