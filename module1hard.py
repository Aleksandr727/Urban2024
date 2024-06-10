# "Школьные учителя устали подсчитывать вручную средний балл каждого ученика, нужно автоматизировать процесс"
# На вход даны следующие даннные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# res = sorted(students)
# print(res)   # Множество students теперь упорядочено по алфавиту

# def имя_функции (аргументы):
#     тело_функции
#     return результат

def get_aver_grade(students: set, grades: list) -> dict:  #Символ «->» в определении функций Python используется для указания ожидаемого типа возвращаемого значения.
    grades_of_students = {}
    students = sorted(students)
    for i in range(len(students)): grades_of_students[students[i]] = sum(grades[i]) / len(grades[i])
    return grades_of_students
res = get_aver_grade(students, grades)
print(res)

# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).