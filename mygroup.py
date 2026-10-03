groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Кузнецова",
        "exams": ["ПИС", "БД", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Анна",
        "surname": "Соколова",
        "exams": ["Информатика", "ОС", "КТП"],
        "marks": [3, 4, 3]
    },
    {
        "name": "Дмитрий",
        "surname": "Попов",
        "exams": ["Философия", "БД", "ПИС"],
        "marks": [3, 3, 4]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


def average(marks):
    return sum(marks) / len(marks)


def filter_students(students, min_average):
    return [student for student in students if average(student["marks"]) > min_average]


if __name__ == "__main__":
    print_students(groupmates)
    print()
    try:
        min_average = float(input("Введите средний балл для фильтрации: ").replace(",", "."))
    except ValueError:
        print("Ошибка: нужно ввести число")
    else:
        result = filter_students(groupmates, min_average)
        print("Студенты со средним баллом выше", min_average, ":")
        if result:
            print_students(result)
        else:
            print("Таких студентов нет")
