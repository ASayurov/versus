from game_data import getdata
from random import randint

data = getdata()
for x in range(len(data)):
    print(data[x].get('name'),)


#Выбираем 1 случайный аккаунт
print(data[randint(0, len(data))])

#Получаем 2ой случайных аккаунта для сравнения

#Сравниваем 2 аккаунта

#Если не удагадали - проиграли

#Если угадали - выводим значение которое угадали и сравниваем с новым значением по не проигрем