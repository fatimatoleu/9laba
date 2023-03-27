#Пример не функциональной программы 
cake_price = 10
cake_ingredients = {"flour": 2, "sugar": 1, "eggs": 3}
cake_profit = 0

pie_price = 8
pie_ingredients = {"flour": 1, "sugar": 0.5, "eggs": 2}
pie_profit = 0

flour_price = 1
sugar_price = 0.5
eggs_price = 0.2

sales = {"cake": 20, "pie": 10}

for item, quantity in sales.items():
    if item == "cake":
        cost = flour_price * cake_ingredients["flour"] + sugar_price * cake_ingredients["sugar"] + eggs_price * cake_ingredients["eggs"]
        revenue = cake_price * quantity
        cake_profit = revenue - cost
    elif item == "pie":
        cost = flour_price * pie_ingredients["flour"] + sugar_price * pie_ingredients["sugar"] + eggs_price * pie_ingredients["eggs"]
        revenue = pie_price * quantity
        pie_profit = revenue - cost

total_profit = cake_profit + pie_profit

print("Общая прибыль: ", total_profit)
