family = dict()
family = {"name": "Jane", "surname": "Doe", "hobbies": ["running", "sky diving", "singing"], "age": 35, 'children': {
    'Alice': {
        "age": 6
    },

    'Bob': {
        "age": 8
    }
}}

print('Есть такое имя' if family.get('children').get('Bob') else 'Нет такого имени')
print(family.get('children').get('Rob', 'Noname'))
