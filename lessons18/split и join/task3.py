template = 'С Днем рождения {name}, сегодня тебе исполнилось {age}, лет'
names = input('Введите имена через запятую: ')
names_list = names.split(', ')

ages = input('Введите возраста через пробел: ')
ages_list = ages.split()

for i_men in range(len(names_list)):
    print(template.format(name=names_list[i_men], age=ages_list[i_men]))


people = [' '.join([names_list[x], ages_list[x]]) for x in range(len(names_list))]

print(people)