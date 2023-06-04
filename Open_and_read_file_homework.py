# import json
# from pprint import pprint
#
# with open('recipes.txt', 'r', encoding='utf-8') as file:
#     cook_book = {}
#     for dishes in file:
#         number_ingredients = int(file.readline())
#         ingredients = []
#         for i in range(number_ingredients):
#             name_ingredient, amount, measure = file.readline().strip().split(' | ')
#             ingredients.append({
#                 'ingredient_name': name_ingredient,
#                 'quantity': amount,
#                 'measure': measure
#             })
#         file.readline()
#         cook_book[dishes.strip()] = ingredients
#
#
# print(json.dumps(cook_book,indent=2,ensure_ascii=False))
#
# def get_shop_list_by_dishes(dishes, person_count):
#     dish_list = {}
#     for dish in dishes:
#         if dish in cook_book:
#             for ing in cook_book[dish]:
#                 if ing['ingredient_name'] in dish_list:
#                     dish_list[ing['ingredient_name']]['quantity'] += int(ing['quantity']) * person_count
#                 else:
#                     dish_list[ing['ingredient_name']] = {'quantity': int(ing['quantity']) * person_count,
#                                                          'measure': ing['measure']}
#
#     print(json.dumps(dish_list, indent=2, ensure_ascii=False))
#
#
# get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)


import os


from pprint import pprint

text_1 = '1.txt'
text_2 = '2.txt'
text_3 = '3.txt'

files = [text_1, text_2, text_3]
file_list = []
for f in files:
    with open(f, 'r', encoding='utf - 8') as file:
        res = file.readlines()
        res.insert(0, f)
        file_list.append(res)

sorted_file_list = sorted(file_list, key=len)
print(sorted_file_list)

with open('4.txt', 'w', encoding='utf - 8') as text_4:
    for file in sorted_file_list:
        text_4.write(file[0])
        text_4.write('\n')
        text_4.write(str(len(file) - 1))
        text_4.write('\n')
        text_4.writelines(file[1:])
        text_4.write('\n')
