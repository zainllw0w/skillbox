mass = [0, 0, 0, 1, 2, 3]
zero = mass.count(0)
new = [x for x in mass if x != 0] + [0] * zero
for _ in range(zero):
    mass.remove(0)

print(new)
print(mass)