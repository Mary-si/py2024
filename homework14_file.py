"""homework 14"""

# Напишите программу, которая создает текстовый файл(если его нету) "students.txt".
# Запишите в файл список студентов, номер группы, их оценки.
# Каждый студент на новой строке. Откройте файл и прочитайте всю информацию из него.
# Напечатайте общее количество студентов, количество студентов для каждой группы
# и среднюю оценку для каждой группы. Допишите эту информацию в конец файла.
# Передусмотрите возможные ошибки и обработайте их.


class Students:
    count_students = 0
    students_by_group = {}

    def __init__(self, surname, group, assessments):
        self.surname = surname
        self.group = group
        self.assessments = assessments
        Students.count_students += 1
        if group in Students.students_by_group:
            Students.students_by_group[group].append(self)
        else:
            Students.students_by_group[group] = [self]

    def __str__(self):
        return f"{self.surname}, {self.group}, {self.assessments}"

    @classmethod
    def inf_all_students(cls):
        try:
            with open("students.txt", "a") as fu:
                fu.write(f"Общее количество студентов: {cls.count_students}")
                print(f"Общее количество студентов: {cls.count_students}")
                for group, students_list in cls.students_by_group.items():
                    count_students_in_group = len(students_list)
                    assessments = [int(st.assessments) for st in students_list]
                    average = sum(assessments) / count_students_in_group
                    print(f"Количество студентов в группе {group}: {count_students_in_group}")
                    print(f"Средняя оценка группы {group}: {average:.2f}")
        except IOError as E:
            print(f"Ошибка: {E}")


student_1 = Students("Mariya Simonenko", "M-091", 3)
student_2 = Students("Ivan Ivanov", "N-031", 4)
student_3 = Students("Kseniya Petrova", "M-091", 5)

try:
    with open("students.txt", "w") as f:
        for student in [student_1, student_2, student_3]:
            student_info = str(student)
            f.write(student_info + "\n")
except IOError as e:
    print(f"Ошибка: {e}")

Students.inf_all_students()
