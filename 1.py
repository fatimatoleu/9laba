#Пример функциональной программы 
def calculate_recipe_cost(recipe, ingredients):
    """
    Функция вычисляет стоимость рецепта на основе цен на ингредиенты.

    recipe: словарь, представляющий рецепт, где ключ - название ингредиента, значение - количество
    ingredients: словарь, представляющий цены на ингредиенты, где ключ - название ингредиента, значение - цена
    return: стоимость рецепта
    """
    total_cost = 0
    for ingredient, amount in recipe.items():
        total_cost += ingredients[ingredient] * amount
    return total_cost

class Bakery:
    """
    Класс, представляющий кондитерскую.
    """
    def __init__(self, name, recipes, ingredients):
        """
        Конструктор класса.

         name: название кондитерской
         recipes: словарь, представляющий рецепты, где ключ - название рецепта, значение - словарь, представляющий ингредиенты и их количество
        ingredients: словарь, представляющий цены на ингредиенты, где ключ - название ингредиента, значение - цена
        """
        self.name = name
        self.recipes = recipes
        self.ingredients = ingredients

    def get_name(self):
        """
        Возвращает название кондитерской.

        return: название кондитерской
        """
        return self.name

    def calculate_profit(self, sales):
        """
        Вычисляет прибыль кондитерской на основе продаж.

         sales: словарь, представляющий продажи, где ключ - название выпечки, значение - количество проданных штук
        return: прибыль кондитерской
        """
        total_profit = 0
        for item, quantity in sales.items():
            total_profit += quantity * (self.recipes[item]["price"] - calculate_recipe_cost(self.recipes[item]["ingredients"], self.ingredients))
        return total_profit

# Пример использования класса Bakery
recipes = {
    "cake": {
        "ingredients": {"flour": 2, "sugar": 1, "eggs": 3},
        "price": 10
    },
    "pie": {
        "ingredients": {"flour": 1, "sugar": 0.5, "eggs": 2},
        "price": 8
    }
}
ingredients = {"flour": 1, "sugar": 0.5, "eggs": 0.2}
bakery = Bakery("Моя пекарня", recipes, ingredients)
sales = {"cake": 20, "pie": 10}
print(bakery.get_name()) # Моя пекарня
print(bakery.calculate_profit(sales)) 
