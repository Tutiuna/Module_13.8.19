ticket = int(input('Ввидите количество билетов: '))
skidka = ticket
summa = 0
cost = 0
while ticket != 0:
    age = int(input('Ввидите возраст участника: '))
    if age >= 18 and age <= 25:
        cost += 990
    elif age > 25:
        cost += 1390
    else:
        cost = 0
    ticket -= 1
summa += cost
if skidka > 3:
    procent = summa * 0.1
    summa = summa - procent
print(round(summa))