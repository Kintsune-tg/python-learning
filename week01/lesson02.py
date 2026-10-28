#Задание №1
name = input("Как вас зовут? ")
print(f"Добрый день, {name}. Длина имени = {len(name)}. Имя заглавными буквами {name.upper()}")

#Задание №2
number1 = input("Какое первое число?")
number2 = input("Какое второе число?")
print(f"Получается {number1} плюс {number2} равно {float(number1)+float(number2)}")

#Задание №3
city = "  Москва  "
clean = city.strip().lower()
print(f"Без пробелов {city.strip()}. Длина строки до изменений {len(city)}. Длина после изменений {len(clean)}. Имя маленькими буквами {clean}")

#Задание №4
age = int(input("Сколько вам лет? "))

if  age >= 18:
    print("Взрослый")
elif age >= 14:
    print("Подросток")
else:
    print("Ребёнок")

#Задание №5

order_sum = float(input("Какая сумма товаров получилась? "))

if order_sum >= 1000:
    print(f"Вы получаете 10% скидки. Ваша сумма составляет {order_sum*0.9}")
elif order_sum >= 500:
    print(f"Вы получаете 5% скидки. Ваша сумма составляет {order_sum*0.95}")
else:
    print(f"Ваша сумма составляет {order_sum}")