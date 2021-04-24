data = dict()

while True:
    text = input('Введите нового пользователя (Фамилия, Имя, номер телефона)').split()
    data[(text[0], text[1])] = text[2]
    print(data)