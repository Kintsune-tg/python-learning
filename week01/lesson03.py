#Задание 1
sales = [100, 400, 200, 500, 300]
print(f"Список значение = {sales}. Минимальное равно {min(sales)}. Максимальное равно {max(sales)}. Сумма значение равно {sum(sales)}. Кол-во элементов {len(sales)}. Первое значение равно {sales[0]}. Последнее значение равно {sales[-1]}")

#Задание 2
sales.append(750)
sales.remove(400)
sales.sort()

print(f"После сортировки: {sales}")
print(f"Есть ли значение 1000? {1000 in sales}")

#Задание 3

total = 0
for s in sales:
    total = total + s
    print(f"Добавили {s}. Накопилось {total}")
print(f"Итого {total}")
print(f"Вручную: {total}, через sum: {sum(sales)}")

#Задание 4
for i in range(1,11):
    print(f"Все числа {i}") #Все подряд

for i in range(1, 11):
    if i % 2 == 0:
        print(f"Четные числа {i}") #Только четные

total = 0
for s in range(1,101): 
    total = total + s
print(f"Сумма значений от 1 до 100 равно {total}") #Сумма значений window sum

#Задание 5

orders = [800, 250, 600, 1200, 1000, 1850, 490, 2800]
total = 0 #Первичное значение сумм заказов больше равно 1000 (ДО РАСЧЕТА)
count = 0 #Первичное количество заказов больше равно 1000 (ДО РАСЧЕТА)
for o in orders:
    if o >= 1000: #Только ЕСЛИ orders >= 1000
        total = total + o #Берет Total = 0 + значение переменной. Сохраняет и переходит к следующему.
        count = count + 1
print(f"Количество заказов больше 1000 равно {count}. Сумма данных заказов равна {total}")