# Через списки
list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]
month = int(input('Какой ваш любимый месяц? Укажите его номер: '))
if month in list_winter:
    print('Зима. Крестьянин, торжествуя, на дровнях обновляет путь...')
elif month in list_spring:
    print('Весна. Еще в полях белеет снег, а воды уж весной шумят...')
elif month in list_summer:
    print('Лето. Лето пахнет земляникой, тёплым дождиком, клубникой.')
elif month in list_autumn:
    print('Осень. Унылая пора... очей очарованье!')

# Через словарь
year_dict = {"Зима": list_winter, "Весна": list_spring, "Лето": list_summer, "Осень": list_autumn}
month = int(input('Какой ваш любимый месяц? Укажите его номер: '))
for key, value in year_dict.items():
    if month in value:
        print(key)
        break
