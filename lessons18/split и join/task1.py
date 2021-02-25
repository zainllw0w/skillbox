user_text = input('Введите 3 слова: ')
user_text_list = user_text.split()

composition_text = 'шла саша по шосе и сосала сушку'
comp_list = composition_text.split()

print('Слово:', str('"')+user_text_list[0]+str('"'), 'встретилось ', comp_list.count(user_text_list[0]), 'раз')
print('Слово:', str('"')+user_text_list[1]+str('"'), 'встретилось ', comp_list.count(user_text_list[1]), 'раз')
print('Слово:', str('"')+user_text_list[2]+str('"'), 'встретилось ', comp_list.count(user_text_list[2]), 'раз')
