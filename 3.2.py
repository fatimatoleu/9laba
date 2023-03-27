from functools import reduce
def get_baked_goods():
    baked_goods = [
        {'name': 'Хлеб', 'ingredients': ['мука', 'дрожжи', 'вода', 'соль'], 'description': 'Ароматный хлеб с золотистой корочкой'},
        {'name': 'Пирог', 'ingredients': ['мука', 'масло', 'сахар', 'яйца', 'варенье'], 'description': 'Сладкий десертный пирог с ягодами'},
        {'name': 'Круассан', 'ingredients': ['мука', 'масло', 'дрожжи', 'вода', 'сахар'], 'description': 'Классический французский завтрак'}
    ]
    return baked_goods

baked_goods_list = get_baked_goods()

# Список всех ингредиентов в выпечке
all_ingredients = reduce(lambda x, y: x + y['ingredients'], baked_goods_list, [])
print(all_ingredients)  # ['мука', 'дрожжи', 'вода', 'соль', 'мука', 'масло', 'сахар', 'яйца', 'варенье', 'мука', 'масло', 'дрожжи', 'вода', 'сахар']
