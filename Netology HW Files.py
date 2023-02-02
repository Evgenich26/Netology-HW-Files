with open('cook_book.txt', 'rt', encoding =  'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        foods_count = int(file.readline())
        foods = []
        for _ in range(foods_count):
            food = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = food 
            foods.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})

        file.readline()
        cook_book[dish_name] = foods

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list_by_dishes = {}
        for dish in dishes:
            dish_ingridients = cook_book[dish]
            for ingridient in dish_ingridients:
                a = ingridient['ingredient_name']
                b = ingridient['measure']
                c = ingridient['quantity']
                x = {}
                x['measure'] = b
                if a not in shop_list_by_dishes:
                    x['quantity'] = int(c) * int(person_count)
                    
                else:
                    d = shop_list_by_dishes[a]
                    e = d['quantity']
                    x['quantity'] =  int(e) + int(c) * int(person_count)
                
                shop_list_by_dishes[a] = x    
              
        return shop_list_by_dishes

    print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
             



def making_list(file_name):
    list = []
    with open(file_name, 'rt', encoding = 'utf-8') as file:
        counter = 0
        for line in file:
            if line:
                counter += 1
        list.append(file_name)
        list.append(str(counter))
    with open(file_name, 'rt', encoding='utf-8') as file:
        text = file.read()
        list.append(text)
    return list

def list_of_lists():
    list_of_lists = []
    list1 = making_list('1.txt')
    list2 = making_list('2.txt')
    list3 = making_list('3.txt')
    list_of_lists.append(list1)
    list_of_lists.append(list2)
    list_of_lists.append(list3)
    list_of_lists.sort(key = lambda x: x[1])

    with open('result.txt', 'w', encoding="utf-8") as f:
        for name, count, text in list_of_lists:
            f.write(f'{name}\n{count}\n{text}\n')

list_of_lists()

