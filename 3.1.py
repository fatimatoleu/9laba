def get_baked_goods():
    baked_goods = [
        {'name': 'Хлеб', 'ingredients': ['мука', 'дрожжи', 'вода', 'соль'], 'description': 'Ароматный хлеб с золотистой корочкой'},
        {'name': 'Пирог', 'ingredients': ['мука', 'масло', 'сахар', 'яйца', 'варенье'], 'description': 'Сладкий десертный пирог с ягодами'},
        {'name': 'Круассан', 'ingredients': ['мука', 'масло', 'дрожжи', 'вода', 'сахар'], 'description': 'Классический французский завтрак'}
    ]
    return baked_goods
baked_goods_list = get_baked_goods()

# Список всех сладких выпечек
sweet_baked_goods = list(filter(lambda x: 'сахар' in x['ingredients'], baked_goods_list))
print(sweet_baked_goods)  # [{'name': 'Пирог', 'ingredients': ['мука', 'масло', 'сахар', 'яйца', 'варенье'], 'description': 'Сладкий десертный пирог с ягодами'}]
