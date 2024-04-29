"""Учебное задание ООП"""


class Student:
    """Класс студентов содержит имя, фамилию, пол, завершенные курсы, курсы в процессе и оценки"""

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """Оцениваем лекторов"""
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Вывод информации по студентам"""
        student_average_rating = self.average_rating_student()
        return (f"Имя: {self.name} \nФамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания: {student_average_rating} \n"
                f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n"
                f"Завершенные курсы: {", ".join(self.finished_courses)}")

    def average_rating_student(self):
        """подсчёт среднего балла по курсам циклом и списком"""
        student_rating = []
        for rating_student in self.grades.values():
            student_rating.append(round((sum(rating_student) / len(rating_student)), 2))
        final_rating = sum(student_rating) / len(student_rating)
        return final_rating


class Mentor:
    """Родительский класс Ментор"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """Возможность ментора ставить оценки студентам"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    """Наследуемый класс Лектор от Ментора"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        """Запрещаю Лектору ставить оценки"""
        return 'Лектор не может выставлять оценки'

    def __str__(self):
        """Вывод информации по Лекторам"""
        lecturer_average_rating = self.average_rating_lecturer()
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {lecturer_average_rating}"

    def average_rating_lecturer(self):
        """подсчёт среднего балла по курсам циклом и списком"""
        lecturer_rating = []
        for rating_lecturer in self.grades.values():
            lecturer_rating.append(round((sum(rating_lecturer) / len(rating_lecturer)), 2))
        final_lecturer_rating = sum(lecturer_rating) / len(lecturer_rating)
        return final_lecturer_rating


class Reviewer(Mentor):
    """Наследуемый класс Ревьюер от Ментора"""

    def __str__(self):
        """Вывод имени и фамилии Ревьюера"""
        return f"Имя: {self.name} \nФамилия: {self.surname}"


def student_average_grade_for_course(students, course):
    """расчёт средней оценки за ДЗ Студентов по курсу"""
    result_students = []
    for student in students:
        for grade in student.grades[course]:
            result_students.append(grade)

    print(f"Средняя оценка за домашние задания по всем студентам в рамках Курса {course}: "
          f"{round((sum(result_students) / len(result_students)), 2)}")


def lecturer_average_grade_for_course(lecturers, course):
    """расчёт средней лекторов"""
    result_lecturer = []
    for lecturer in lecturers:
        for grade in lecturer.grades[course]:
            result_lecturer.append(grade)

    print(f"Средняя оценка за лекции всех лекторов в рамках Курса {course}: "
          f"{round((sum(result_lecturer) / len(result_lecturer)), 2)}")


"""Тестовые данные для проверки"""
student1 = Student("Илья", "Иванов", "м")
student2 = Student("Мария", "Петрова", "ж")
student3 = Student("Максим", "Умничка", "м")
lecturer1 = Lecturer("Алексей", "Смирнов")
lecturer2 = Lecturer("Елена", "Козлова")
reviewer1 = Reviewer("Андрей", "Кузнецов")
reviewer2 = Reviewer("Ольга", "Соколова")

student1.courses_in_progress += ["Python", "HTML", "English"]
student1.finished_courses += ["Javascript"]
student2.courses_in_progress += ["Python", "HTML"]
student2.finished_courses += ["Java"]
student3.courses_in_progress += ["Python"]
lecturer1.courses_attached += ["HTML", "Javascript"]
lecturer2.courses_attached += ["Python", "Java", "HTML"]
reviewer1.courses_attached += ["HTML", "Python", "Javascript"]
reviewer2.courses_attached += ["Java", "CSS"]

student1.rate_lecturer(lecturer2, "Python", 8)
student1.rate_lecturer(lecturer2, "HTML", 6)
student2.rate_lecturer(lecturer2, "Python", 7)
student2.rate_lecturer(lecturer1, "HTML", 9)

reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "HTML", 9)
reviewer1.rate_hw(student2, "Python", 9)
reviewer1.rate_hw(student2, "HTML", 7)
reviewer1.rate_hw(student3, "Python", 10)

print(student1, student2, student3, sep="\n\n", end="\n\n")
print(lecturer1, lecturer2, sep="\n\n", end="\n\n")
print(reviewer1, reviewer2, sep="\n\n", end="\n\n")

'''Сравнение по рейтингу между студентами и лекторами'''
print(f"Средний балл {student1.average_rating_student()} студента {student1.name} больше среднего балла "
      f"{student3.average_rating_student()} студента {student3.name} - "
      f"{student1.average_rating_student() > student3.average_rating_student()}")
print(f"Средний балл {lecturer1.average_rating_lecturer()} лектора {lecturer1.name} больше среднего балла "
      f"{lecturer2.average_rating_lecturer()} лектора {lecturer2.name} - "
      f"{lecturer1.average_rating_lecturer() > lecturer2.average_rating_lecturer()}")

print("\n")
'''Средняя оценка студентов и лекторов'''
student_average_grade_for_course([student1, student2, student3], "Python")
lecturer_average_grade_for_course([lecturer1, lecturer2], "HTML")
