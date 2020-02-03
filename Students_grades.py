'''
В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести
средний балл по классу. Так же,
записать в новый файл всех учащихся в формате "Фамилия И. Ср. балл":
'''


from string import ascii_letters

# file = open('students.txt', 'r')
# print(file.read())
# line = file.read()
#
# str_names = ""
# str_grades = ""

# studs = {}
# s = 0
# for i in file:
#     sname = input(str(i+1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[sname] = point
#     s += point
# print(i)


# lines = 0
#
# for line in file:
#     lines += 1
#
# print(lines)
#
# file.close()
# # print(line)

# for linee in file:
#     for c in linee:
#         if c.isdigit():
#             print( )
#         print(c)

lst = []
lst_lst = []


with open('students.txt', 'r') as s:
    for line in s:
        lst.extend([line.strip().split(';')])
    print(lst)

# for i in lst:
#     lst_lst.extend([i.split(' ')])
# print(lst_lst)

for linee in lst:
    for c in linee:
        for a in c:
            if a.isdigit():
                print(a, end=' ')

print()
    # print(c)
    #         print(linee)

for i in lst:
    lst[i] = list(lst[i])

print(i)