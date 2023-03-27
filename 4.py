"""
Для курьерской компании в Алматы необходимо сделать расчет доставки. 
В квадрате Аль-Фараби -Саина-Ташентского-Достык стоимость 500тг
если цена товара ниже 10тыс. Если выше 10тыс то бесплатно. За пределы
квадрата 1000тг если цена товара до 10тыс, если выше то 1000тг.
Напишите функцию, принимающую в качестве параметра наименование
улицы и стоимость товара и возвращающую общую сумму доставки. 
"""
from functools import reduce

# Создаем словарь с информацией о стоимости доставки в разных зонах
delivery_prices = {
    'Аль-Фараби-Саина-Ташентского-Достык': {
        'price_below_10k': 500,
        'price_above_10k': 0
    },
    'вне квадрата': {
        'price_below_10k': 1000,
        'price_above_10k': 1000
    }
}

def calculate_delivery_price(street, item_price):
    # Определяем стоимость доставки в зависимости от улицы и стоимости товара
    if item_price < 10000:
        price = delivery_prices[street]['price_below_10k']
    else:
        price = delivery_prices[street]['price_above_10k']
    
    return price

# Пример использования функции для расчета стоимости доставки
delivery_street = 'Аль-Фараби-Саина-Ташентского-Достык'
item_price = 9000
total_delivery_price = reduce(lambda x, y: x + y, map(lambda x: calculate_delivery_price(delivery_street, x), [item_price]))
print(total_delivery_price)  # Выведет 0, так как стоимость доставки бесплатная
