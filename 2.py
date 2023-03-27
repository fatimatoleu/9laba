#Напишите функцию в результате которая возвращает список, кортежи слоаварь. Пример должен быть индивидуальным.
def get_baked_goods():
    baked_goods = [
        {
            "name": "Хлеб",
            "ingredients": ["мука", "дрожжи", "вода", "соль"],
            "description": "Основное блюдо на столе"
        },
        {
            "name": "Пирог",
            "ingredients": ["мука", "масло", "сахар", "яйца", "варенье"],
            "description": "Сладкий десертный пирог с ягодами"
        },
        {
            "name": "Круассан",
            "ingredients": ["мука", "масло", "дрожжи", "вода", "сахар"],
            "description": "Легкий французский завтрак"
        }
    ]
    
    return baked_goods
baked_goods_list = get_baked_goods()
print(baked_goods_list)

