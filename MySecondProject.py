class Student: # Конструктор класса Студент
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()
    
    def rate_hw(self, lecturer, course, grade): # метод для выставления оценки лектора студентом
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def __str__(self): # метод для вывода информации по студенту
        for с, val in self.grades.items():
            self.average_grade = (sum(val)/len(val))
        return   f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за домашнее задание: {self.average_grade}\n' \
                 f'Курсы в процессе обучения: {self.courses_in_progress}\n' \
                 f'Завершенные курсы: {self.finished_courses}'
    
    def __lt__(self, other):
        """Реализует сравнение через операторы '<,>' студентов между собой по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f"Имя: {self.name}\n"\
            f"Фамилия: {self.surname}\n"
 
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade): 
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return super().__str__()
                

class Lecturer(Mentor):
    def __init__(self, name, surname, average_grade = 0):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.average_grade = average_grade
              
    def __str__(self):
        for с, val in self.grades.items():
            self.average_grade = (sum(val)/len(val))
        return f"Имя: {self.name}\n"\
            f"Фамилия: {self.surname}\n"\
            f"Средняя оценка за лекции: {self.average_grade}\n"

    def __lt__(self, other):
        """Реализует сравнение через операторы '<,>' лекторов между собой по средней оценке за лекции"""
        if not isinstance(other, Lecturer):
            print('некорректно')
            return
        return self.average_grade < other.average_grade



first_student = Student('Jack', 'Hart') # Создаем первого студента
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Введение в программирование',]
 
second_student = Student('Sasha', 'Abramov') # Создаем второго студента
second_student.courses_in_progress += ['Python']
second_student.finished_courses += ['Введение в программирование']


first_lecturer = Lecturer('Some', 'Buddy') # Создаем первого лектора
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer("Victor", "Andreev") # Создаем второго лектора
second_lecturer.courses_attached += ['Python']



first_reviewer = Reviewer('John', 'Smith') # Создаем первого проверяющего
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Ivan', 'Smirnov') # Создаем второго проверяющего
second_reviewer.courses_attached += ['Основы алгоритмов']



#Выставление оценок студентам
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Основы алгоритмов', 22)
second_reviewer.rate_hw(first_student, 'Основы алгоритмов', 20)
second_reviewer.rate_hw(first_student, 'Основы алгоритмов', 18)


first_reviewer.rate_hw(second_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 16)
second_reviewer.rate_hw(second_student, 'Основы алгоритмов', 15)
second_reviewer.rate_hw(second_student, 'Основы алгоритмов', 10)
second_reviewer.rate_hw(second_student, 'Основы алгоритмов', 15)

# Выставление оценкок лекторам
first_student.rate_hw(first_lecturer, 'Python', 2) 
first_student.rate_hw(first_lecturer, 'Основы алгоритмов', 7)

second_student.rate_hw(second_lecturer, 'Python', 2) 
second_student.rate_hw(second_lecturer, 'Основы алгоритмов', 12)

print("Cтуденты:")
print()
print(first_student)
print()
print(second_student)
print()
print("******************")
print()
print("Проверяющие:")
print()
print(first_reviewer)
print()
print(second_reviewer)
print()
print("******************")
print()
print("Лекторы:")
print()
print(first_lecturer)
print()
print(second_lecturer)

print("\n******************\n")

#Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
       f'{first_lecturer.name} {first_lecturer.surname} < {second_lecturer.name} {second_lecturer.surname} = {first_lecturer < second_lecturer}')
print()
#Выводим результат сравнения студентов по средним оценкам за ДЗ
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
       f'{first_student.name} {first_student.surname} < {second_student.name} {second_student.surname} = {first_student < second_student}')
print()

#cоздаем список студентов
student_list = [first_student, second_student]

#создаем список лекторов
lecturer_list = [first_lecturer, second_lecturer]

#создаем функцию для подсчета средней оценки всех студентов в рамках конкретного курса
def student_average_grades(student_list, course_name):
     sum_all = 0
     count_all = 0
     for stud in student_list:
        if stud.courses_in_progress == [course_name]:
             sum_all += stud.average_grade
             count_all += 1
     average_for_all = sum_all / count_all
     return average_for_all

#создаем функцию для подсчета средней оценки всех лекторов в рамках конкретного курса
def lecturers_average_grades(lecturer_list, course_name):
     sum_all = 0
     count_all = 0
     for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
             sum_all += lect.average_grade
             count_all += 1
     average_for_all = sum_all / count_all
     return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_average_grades(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturers_average_grades(lecturer_list, 'Python')}")

