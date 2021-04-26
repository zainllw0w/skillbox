text = input('Введите текст: ')


if text.isdigit():
    print(f"Это тип: int\nid: {id(text)} \nОбьект: immutable (неизмениемый)")
elif isinstance(text, str):
    print(f"Это тип: СТР\nid: {id(text)} \nОбьект: immutable (неизмениемый)")
elif isinstance(text, set):
    print(f"Это тип: set\nid: {id(text)} \nОбьект: mutable (измениемый)")
elif isinstance(text, list):
    print(f"Это тип: list\nid: {id(text)} \nОбьект: mutable (измениемый)")
elif isinstance(text, dict):
    print(f"Это тип: dict\nid: {id(text)} \nОбьект: mutable (измениемый)")