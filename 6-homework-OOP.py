class Student:

  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    self.average_grade = {}

  def rate_lectur(self, lecturer, course, lecture_grade):
    if isinstance(
        lecturer, Lecturer
    ) and course in self.courses_in_progress or self.finished_courses and course in lecturer.courses_attached:
      if course in lecturer.lecture_grades:
        lecturer.lecture_grades[course].append(lecture_grade)
        lecturer.average_grade[course] = [
          sum(lecturer.lecture_grades[course]) /
          len(lecturer.lecture_grades[course])
        ]
      else:
        lecturer.lecture_grades[course] = [lecture_grade]
    else:
      print("ERROR")

  def average_all_grade(self):
    if not self.grades:
      return 0
    average_grade = []
    for assessment in self.grades.values():
      average_grade.extend(assessment)
    return sum(average_grade) / len(average_grade)

  def __lt__(self, other):
    if not isinstance(other, Student):
      return "Такое сравнение не корректно"
    return self.average_all_grade() < other.average_all_grade()

  def __str__(self):
    return f"Студент\nИмя: {self.name}" \
           f"\nФамилия: {self.surname}" \
           f"\nСредняя оценка за курс {', '.join(f'{key}: {round(values[0], 2)}' for key, values in self.average_grade.items())}" \
           f"\nСредняя оценка за все курсы : {round(self.average_all_grade(), 2)}" \
           f"\nКурсы в процессе обучения: {', '.join(self.courses_in_progress)}" \
           f"\nЗавершённые курсы: {', '.join(self.finished_courses)}\n"


class Mentor:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []


class Lecturer(Mentor):

  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.lecture_grades = {}
    self.average_grade = {}

  def average_all_grade(self):
    if not self.lecture_grades:
      return 0
    average_lecture_grade = []
    for assessment in self.lecture_grades.values():
      average_lecture_grade.extend(assessment)
    return sum(average_lecture_grade) / len(average_lecture_grade)

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      return "Такое сравнение не корректно"
    return self.average_all_grade() < other.average_all_grade()

  def __str__(self):
    return f"Лектор курса: {', '.join(self.courses_attached)}" \
           f"\nИмя: {self.name}" \
           f"\nФамилия: {self.surname}" \
           f"\nСредняя оценка за лекции по курсу: {', '.join(f'{key}: {round(values[0],2)}' for key, values in self.average_grade.items())}" \
           f"\nСредняя оценка за все лекции: {self.average_all_grade()}\n"


class Reviewer(Mentor):

  def rate_homework(self, student, course, grade):
    if isinstance(
        student, Student
    ) and course in self.courses_attached and course in student.courses_in_progress or student.finished_courses:
      if course in student.grades:
        student.grades[course].append(grade)
        student.average_grade[course] = [
          sum(student.grades[course]) / len(student.grades[course])
        ]
      else:
        student.grades[course] = [grade]
    else:
      print('Ошибка')

  def __str__(self):
    return f"Рецензент курса: {', '.join(self.courses_attached)}\nИмя: {self.name}\nФамилия: {self.surname}\n"


#Имя, фамилия, пол студента и что изучал/изучает
student_1 = Student('Наруто', 'Узумаки', 'Мужчина')
student_1.courses_in_progress.append('Python')
student_1.finished_courses.append('C++')
student_1.finished_courses.append('JavaScript')
student_1.finished_courses.append("Основы программирования")

#Имя, фамилия, пол студента и что изучал/изучает
student_2 = Student('Александра', 'Паучкова', 'Женщина')
student_2.courses_in_progress.append('Python')
student_2.finished_courses.append('JavaScript')
student_2.finished_courses.append("Основы программирования")

#Имя, фамилия, пол студента и что изучал/изучает
student_3 = Student('Кен', 'Каннеки', 'Мужчина')
student_3.courses_in_progress.append('JavaScript')
student_3.finished_courses.append('C++')
student_3.finished_courses.append("Основы программирования")

#Имя, фамилия лектора и какие курсы приподаёт
PJ_lecturer1 = Lecturer('Фатима', 'Ахмедова')
PJ_lecturer1.courses_attached.append('Python')
PJ_lecturer1.courses_attached.append('JavaScript')
PJ_lecturer1.courses_attached.append("Основы программирования")

#Имя, фамилия лектора и какие курсы приподаёт
PJ_lecturer2 = Lecturer('Влад', 'Бумага')
PJ_lecturer2.courses_attached.append('Python')
PJ_lecturer2.courses_attached.append('JavaScript')

#Имя, фамилия лектора и какие курсы приподаёт
C_lecturer1 = Lecturer('Данил', 'Микрон')
C_lecturer1.courses_attached.append('C++')
C_lecturer1.courses_attached.append('C')
C_lecturer1.courses_attached.append('C#')
C_lecturer1.courses_attached.append("Основы программирования")

#Имя, фамилия лектора и какие курсы приподаёт
C_lecturer2 = Lecturer('Всемир', 'Окурок')
C_lecturer2.courses_attached.append('C++')
C_lecturer2.courses_attached.append('C')
C_lecturer2.courses_attached.append('C#')

#Имя, фамилия рецензента и по каким курсам проверяет
C_reviewer1 = Reviewer('Дмитрий', 'Зажерило')
C_reviewer1.courses_attached.append('C++')
C_reviewer1.courses_attached.append('C')
C_reviewer1.courses_attached.append('C#')

#Имя, фамилия рецензента и по каким курсам проверяет
C_reviewer2 = Reviewer('Яна', 'Цист')
C_reviewer2.courses_attached.append('C++')
C_reviewer2.courses_attached.append('C')
C_reviewer2.courses_attached.append('C#')

#Имя, фамилия рецензента и по каким курсам проверяет
PJ_reviewer1 = Reviewer('Лена', 'Головач')
PJ_reviewer1.courses_attached.append('Python')
PJ_reviewer1.courses_attached.append('JavaScript')

#Имя, фамилия рецензента и по каким курсам проверяет
PJ_reviewer2 = Reviewer('Вова', 'Вист')
PJ_reviewer2.courses_attached.append('Python')
PJ_reviewer2.courses_attached.append('JavaScript')

#Оценки 1 студента по курсам
PJ_reviewer1.rate_homework(student_1, 'Python', 9)
PJ_reviewer2.rate_homework(student_1, 'Python', 10)
PJ_reviewer1.rate_homework(student_1, 'JavaScript', 8)
PJ_reviewer2.rate_homework(student_1, 'JavaScript', 6)
C_reviewer1.rate_homework(student_1, 'C++', 10)
C_reviewer2.rate_homework(student_1, 'C++', 9)

#Оценки 2 студента по курсам
PJ_reviewer1.rate_homework(student_2, 'Python', 9)
PJ_reviewer2.rate_homework(student_2, 'Python', 6)
PJ_reviewer1.rate_homework(student_2, 'JavaScript', 9)
PJ_reviewer2.rate_homework(student_2, 'JavaScript', 7)

#Оценки 3 студента по курсам
C_reviewer1.rate_homework(student_3, 'C++', 5)
C_reviewer2.rate_homework(student_3, 'C++', 6)
PJ_reviewer1.rate_homework(student_3, 'JavaScript', 9)
PJ_reviewer1.rate_homework(student_3, 'JavaScript', 7)

#Оценки лекции от 1 студента по курсам
student_1.rate_lectur(PJ_lecturer1, 'Python', 10)
student_1.rate_lectur(PJ_lecturer2, 'Python', 9)
student_1.rate_lectur(PJ_lecturer1, 'JavaScript', 8)
student_1.rate_lectur(PJ_lecturer2, 'JavaScript', 9)
student_1.rate_lectur(C_lecturer1, 'C++', 10)
student_1.rate_lectur(C_lecturer2, 'C++', 9)

#Оценки лекции от 2 студента по курсам
student_2.rate_lectur(PJ_lecturer1, 'Python', 6)
student_2.rate_lectur(PJ_lecturer2, 'Python', 5)
student_2.rate_lectur(PJ_lecturer1, 'JavaScript', 7)
student_2.rate_lectur(PJ_lecturer2, 'JavaScript', 8)

#Оценки лекции от 3 студента по курсам
student_3.rate_lectur(C_lecturer1, 'C++', 10)
student_3.rate_lectur(C_lecturer2, 'C++', 9)
student_3.rate_lectur(PJ_lecturer1, 'JavaScript', 5)
student_3.rate_lectur(PJ_lecturer2, 'JavaScript', 10)

#Вывод информации
print(f"Список студентов:\n\n{student_1}\n{student_2}\n{student_3}\n")
print(
  f"Списор лекторов:\n\n{PJ_lecturer1}\n{PJ_lecturer2}\n{C_lecturer1}\n{C_lecturer2}"
)
print(
  f"Список рецензентов:\n\n{PJ_reviewer1}\n{PJ_reviewer2}\n{C_reviewer1}\n{C_reviewer2}"
)
#Список студентов
student_list = [student_1, student_2, student_3]
#Список лекторов
lecturer_list = [PJ_lecturer1, PJ_lecturer2, C_lecturer1, C_lecturer2]


#Функция подсчёта среднего оценки по курсу всех студентов
def average_grade_on_the_course(persons, course):
  if not isinstance(persons, list):
    return "Not list"
  all_average_grade = []
  for person in persons:
    all_average_grade.extend(person.average_grade.get(course, []))
  if not all_average_grade:
    return "По такому курсу ни у кого нет оценок"
  return round(sum(all_average_grade) / len(all_average_grade), 2)


print("Все курсы: Python, JavaScript, C++")
course_name = input("Введите название курса: ")
print(
  f"Средняя оценка всех студентов по курсу {course_name}: {average_grade_on_the_course(student_list, course_name)}"
)
print(
  f"Средняя оценка всех лекций по курсу {course_name}: {average_grade_on_the_course(lecturer_list, course_name)}"
)