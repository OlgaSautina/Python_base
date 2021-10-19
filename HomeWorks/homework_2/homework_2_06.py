"""
# пример списка товаров из задания
list_products = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
"""
# 1 этап - формируем список товаров
list_products = []
n = 3
i = 1
while i <= n:
    print(f'Заполните характеристики товара № {i}.')
    dict_product = dict()
    dict_product['название'] = input('Название: ')
    dict_product['цена'] = int(input('Цена: '))
    dict_product['количество'] = int(input("Количество: "))
    dict_product['ед'] = input("Единица измерения: ")
    tuple_product = (i, dict_product)
    list_products.append(tuple_product)
    i += 1

print(list_products)
# 2 этап - проводим аналитку
dict_analytics = {}
for product in list_products:
    dict_product = product[1]
    for key, value in dict_product.items():
        if key in dict_analytics.keys():
            list_values = list()
            list_values = dict_analytics.get(key)
            list_values.append(value)
            dict_analytics[key] = list_values
        else:
            list_values = list()
            list_values.append(value)
            dict_analytics[key] = list_values

# исключим повторяющиеся значения - пропусканием списка значений через set
for key, value in dict_analytics.items():
    dict_analytics[key] = list(set(value))

print(dict_analytics)
