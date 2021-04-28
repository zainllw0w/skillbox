import copy
site = {

    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def f(n,data=site, new_list =list()):
  if n == 0:
    return
  name = input('Введите название сайта:')
  data['html']['head']['title'] = f'куплю\продам {name} не дорого'
  data['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
  new_list.append(str(data))
  for i in new_list:
    print(i)
  f(n-1)

f(2)




