day_all = 0
day_a = int(input('Введите кол-во километров а: '))
day_b = int(input('Введите кол-во километров б: '))
while day_a < day_b:
    day_a = day_a * 1.1
    day_all += 1
print(f"Нужно дней - {day_all}")
