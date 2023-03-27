#Приведите свой пример с использованием функций Map, Filter и Reduce. Выясните отличия.
def get_baked_goods():
    baked_goods = [
        {'name': 'Хлеб', 'ingredients': ['мука', 'дрожжи', 'вода', 'соль'], 'description': 'Ароматный хлеб с золотистой корочкой'},
        {'name': 'Пирог', 'ingredients': ['мука', 'масло', 'сахар', 'яйца', 'варенье'], 'description': 'Сладкий десертный пирог с ягодами'},
        {'name': 'Круассан', 'ingredients': ['мука', 'масло', 'дрожжи', 'вода', 'сахар'], 'description': 'Классический французский завтрак'}
    ]
    return baked_goods
baked_goods_list = get_baked_goods()

# Список всех названий выпечки в верхнем регистре
baked_goods_names = list(map(lambda x: x['name'].upper(), baked_goods_list))
print(baked_goods_names)  # ['ХЛЕБ', 'ПИРОГ', 'КРУАССАН']

