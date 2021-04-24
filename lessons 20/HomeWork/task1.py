students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },

    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },

    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dictt):
    interests = set()
    group = dict()
    lensurname = 0
    for id, basekey in dictt.items():
        for i in basekey['interests']:
            interests.add(i)
        lensurname += len(basekey['surname'])
        group[id] = basekey['age']

    return interests, lensurname, group








my_lst, l, group = f(students)

print(group)
print(my_lst, l)

