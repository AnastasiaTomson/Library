from models import *
from datetime import date, timedelta


# Создать студента
def test_local_repo_student_service_can_create_user():
    depart = create_depart(1, "Гриффиндор", "+7(000)777-77-77")
    student = create_student(1, '1111111111', 'Петров Петр Петрович', depart)
    assert isinstance(student, Student)
    assert student.fio == 'Петров Петр Петрович'


# Создать факультет
def test_local_repo_depart_can_create_depart():
    depart = create_depart(1, "Гриффиндор", "+7(000)777-77-77")
    assert isinstance(depart, Depart)
    assert depart.name == 'Гриффиндор'


# Создать автора
def test_local_repo_author_can_create_author():
    author = create_author(1, "Александр Сергеевич Пушкин")
    assert isinstance(author, Author)
    assert author.fio == 'Александр Сергеевич Пушкин'


# Создать издательство
def test_local_repo_publish_can_create_publish():
    publish = create_publish(1, "Москва", "Махаон")
    assert isinstance(publish, Publish)
    assert publish.name == 'Махаон'


# Создать книгу
def test_local_repo_book_can_create_book():
    author = create_author(1, "Александр Сергеевич Пушкин")
    publish = create_publish(1, "Москва", "Махаон")
    book = create_book(1, 20, "Евгений Онегин", 7, author, publish)
    assert book.title == "Евгений Онегин"


# Забронировать книгу
def test_local_repo_reserve_can_create_reserve():
    create_depart(1, "Гриффиндор", "+7(000)777-77-77")  # Создание факультета
    student = create_student(1, '+6(666) 66-66-66', 'Гарри Джеймс Поттер ', 1)  # Создание студента
    author = create_author(1, "Александр Сергеевич Пушкин")  # Создание автора
    publish = create_publish(1, "Москва", "Махаон")  # Создание издательства
    book = create_book(1, 10, "Евгений Онегин", 7, author, publish)  # Создание книги
    book.reserve(Reserve(1, date.today(), student.student_id))  # Бронирование книги
    assert book.allocated_quantity == 1
    assert book.available_quantity == 9


# Получить книгу
def test_local_repo_issue_can_create_issue():
    create_depart(1, "Гриффиндор", "+7(000)777-77-77")  # Создание факультета
    student = create_student(1, '+6(666) 66-66-66', 'Гарри Поттер ', 1)  # Создание студента
    student2 = create_student(2, '+4(444) 44-44-44', 'Гермиона Грейнджер ', 1)  # Создание студента

    author = create_author(1, "Александр Сергеевич Пушкин")  # Создание автора
    publish = create_publish(1, "Москва", "Махаон")  # Создание издательства

    book1 = create_book(1, 10, "Евгений Онегин", 100, author, publish)  # Создание книги
    book2 = create_book(2, 2, "Борис Годунов", 157, author, publish)  # Создание книги

    book1.reserve(Reserve(1, date.today(), student.student_id))  # Бронирование книги
    book1.issue(Issue(1, date.today(), date.today() + timedelta(days=30), student.student_id))  # Получение забронированной книги

    book2.issue(Issue(2, date.today(), date.today() + timedelta(days=30), student.student_id))  # Получение не забронированной книги

    book2.reserve(Reserve(2, date.today(), student2.student_id))  # Бронирование книги

    assert book1.allocated_quantity == 1  # Проверка сколько книг забронировано и на руках
    assert book1.available_quantity == 9  # Проверка кол-ва книг в наличии

    assert book2.allocated_quantity == 2  # Проверка сколько книг забронировано и на руках
    assert book2.available_quantity == 0  # Проверка кол-ва книг в наличии
