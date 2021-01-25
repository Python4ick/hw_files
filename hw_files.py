cook_book = {}


def get_cook_book(file):
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line != '':
                dish_name = line.strip()
                ingredients_numbers = int(f.readline().strip())
                ingredient_list = []
                for i in range(ingredients_numbers):
                    ingredient_about = f.readline().strip().split(' | ')
                    ingredient, quantity, measure = ingredient_about
                    ingredient_list += [{'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure}]
                cook_book.setdefault(dish_name, ingredient_list)
                f.readline()
                continue
            else:
                break


def print_cook_book(book):
    for dish, ingredients in book.items():
        print(dish)
        for ingredient in ingredients:
            print(ingredient)


# В этой фунцкии учтен повтор игредиентов (в if)
def get_shop_list_by_dishes(dishes, person_count):
    list_of_products = {}

    for dish in dishes:
        for recipe in cook_book[dish]:
            ingredient = recipe['ingredient_name']
            measure = recipe['measure']
            quantity = int(recipe['quantity']) * person_count
            if ingredient in list_of_products:
                quantity += int(list_of_products[ingredient]['quantity'])
                list_of_products[ingredient].update(quantity=quantity)
            else:
                list_of_products.setdefault(ingredient, {'measure': measure, 'quantity': quantity})

    for ingredient, about in list_of_products.items():
        print(ingredient, about)
    # return list_of_products <- можно return, но я решил вывести результат в читаемом виде двумя строками выше


get_cook_book('recipes.txt')
print_cook_book(cook_book)

# Напечатаем разделитель строки и добавим в список блюдо с повторяющимся ингредиентом для проверки работы алгоритма
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
