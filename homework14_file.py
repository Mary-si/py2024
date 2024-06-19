"""homework 14"""

# Напишите программу, которая создает текстовый файл
# (если его нету) "students.txt".
# Запишите в файл список студентов, номер группы, их оценки.
# Каждый студент на новой строке. Откройте файл и
# прочитайте всю информацию из него.
# Напечатайте общее количество студентов,
# количество студентов для каждой группы
# и среднюю оценку для каждой группы. Допишите эту информацию в конец файла.
# Передусмотрите возможные ошибки и обработайте их.


class Students:
    """студенты"""
    count_students = 0
    students_by_group: dict[str, list['Students']] = {}

    def __init__(self, surname, group, assessments):
        """информация о студентах"""
        self.surname = surname
        self.group = group
        self.assessments = assessments
        Students.count_students += 1
        if group in Students.students_by_group:
            Students.students_by_group[group].append(self)
        else:
            Students.students_by_group[group] = [self]

    def __str__(self):
        """общая информация о студентах"""
        return f"{self.surname}, {self.group}, {self.assessments}"

    @classmethod
    def inf_all_students(cls):
        """общее количество студентов, количество студентов для каждой группы
        и среднюю оценку для каждой группы"""
        try:
            with open("students.txt", "a", encoding="utf-8") as fu:
                fu.write(f"Общее количество студентов: {cls.count_students}")
                print(f"Общее количество студентов: {cls.count_students}")
                for group, students_list in cls.students_by_group.items():
                    count_students_in_group = len(students_list)
                    assessments = [int(st.assessments) for st in students_list]
                    average = sum(assessments) / count_students_in_group
                    print(f"Количество студентов в группе"
                          f"{group}: {count_students_in_group}")
                    print(f"Средняя оценка группы {group}: {average:.2f}")
        except IOError as list_s:
            print(f"Ошибка: {list_s}")


student_1 = Students("Mariya Simonenko", "M-091", 3)
student_2 = Students("Ivan Ivanov", "N-031", 4)
student_3 = Students("Kseniya Petrova", "M-091", 5)

try:
    with open("students.txt", "w", encoding="utf-8") as f:
        for student in [student_1, student_2, student_3]:
            STUDENT_INFO = str(student)
            f.write(STUDENT_INFO + "\n")
except IOError as e:
    print(f"Ошибка: {e}")

Students.inf_all_students()
