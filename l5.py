izd = int(input('Введите издержки: '))
v = int(input('Введите выручку: '))
if izd > v:
    print("У вас издержки")
elif izd == v:
    print("Издержки и прибыль равны")
else:
    print("У вас прибыль")
