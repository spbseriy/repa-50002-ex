grades = [4, 5, 3, 5, 4, 2, 5, 3, 4]


#•	Найти средний балл.
average = sum(grades)/len(grades)
print("среднее", average)

#•	Определить количество пятерок.
count_5 = grades.count(5)
print('Кол-во 5-к:',count_5)
#•	Вывести список без двоек.
filter = [OCENKA for OCENKA in grades if OCENKA != 2 ]
print('Без двоек', filter)
