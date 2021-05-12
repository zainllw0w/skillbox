def mean(data):
    return float(sum(data)) / len(data)


class Student:
    def __init__(self, index, fi, ngroup, rait):
        self.i = index
        self.fi = fi
        self.ngroup = ngroup
        self.rait = rait

    def mean(self):
        self.srarf = mean(self.rait)

    def info(self):
        print(f'name: {self.fi}\n bal: {self.srarf}')


students = list()

for i in range(5):
    print(f'Введите фамилию студента {i + 1}', end='')
    name = input()
    print(f'Введите группу студента {i + 1}', end='')
    gr = input()
    print(f'Введите 5 оценок за предметы через пробел', end='')
    bal = list(map(int, input().split()))
    while len(bal) > 5 or len(bal) < 5:
        print('Сказано введите 5 балов!!')
        bal = list(map(int, input().split()))
    students.append(Student(i + 1, name, gr, bal))

for st in students:
    st.mean()

for st in sorted(students, key=lambda student: student.srarf, reverse=True):
    print(f'{st.fi} со средним балом: {st.srarf}')
