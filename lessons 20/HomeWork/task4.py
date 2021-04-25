players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


itog = list()
for key, value in players.items():
    new_list = list()
    new_list += [x for x in key]
    new_list += [x for x in value]
    new_list = tuple(new_list)
    itog.append(new_list)
print(itog)

