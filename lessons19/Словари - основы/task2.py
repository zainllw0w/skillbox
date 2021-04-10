student_input = input('Введите информацию о студенте через пробел: фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки\n').split()

student_info = dict()

student_info['Фамилия'] = student_input[0]
student_info['Имя'] = student_input[1]
student_info['Город'] = student_input[2]
student_info['Вуз'] = student_input[3]
student_info['Оценки'] = []

for i in student_input[4:]:
    student_info['Оценки'].append(i)

for i in student_info:
    print(i, ':', student_info[i])


