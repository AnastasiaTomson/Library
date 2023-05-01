import datetime
from typing import List
from datetime import date, timedelta
from dataclasses import dataclass


class Depart:
    """ Факультет """

    def __init__(self, phone: str, name: str):
        self.phone = phone  # телефон
        self.name = name  # наименование

    def __eq__(self, other):
        if isinstance(other, Depart):
            return self.name == other.name
        else:
            return False


class Author:
    """ Автор """

    def __init__(self, fio: str):
        self.fio = fio  # ФИО

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.fio == other.fio
        else:
            return False


class Publish:
    """ Издательство """

    def __init__(self, town: str, name: str):
        self.town = town  # город
        self.name = name  # наименование

    def __eq__(self, other):
        if isinstance(other, Publish):
            return self.town == other.town
        else:
            return False


class Student:
    """ Студент """

    def __init__(self, num: str, fio: str, depart: Depart):
        self.num = num  # номер зачетной книжки
        self.fio = fio  # ФИО
        self.depart = depart  # факультет

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        else:
            return False


class Book:
    """ Книга """

    def __init__(self, amount: int, title: str, author: Author, publish: Publish):
        self.title = title
        self.author = author
        self._amount = amount  # кол-во экземпляров
        self.publish = publish  # издательство

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        else:
            return False


class Reserve:
    """ Резервирование """

    def __init__(self, student: int):
        self.student = student
        self.date_reserve = datetime.datetime.today()  # кол-во экземпляров

    def __eq__(self, other):
        if isinstance(other, Reserve):
            return self.title == other.title
        else:
            return False


class ReserveBook:
    """ Книги в резерве """

    def __init__(self, book: Book, reserve: Reserve):
        self.book = book
        self.reserve = reserve

    def __eq__(self, other):
        if isinstance(other, ReserveBook):
            return self.book == other.book and self.reserve == other.reserve
        else:
            return False


def create_student(num: str, fio: str, depart: Depart):
    student = Student(num, fio, depart)
    return student


def create_depart(name: str, phone: str):
    depart = Depart(phone, name)
    return depart


def create_author(fio: str):
    author = Author(fio)
    return author


def create_publish(publish_id: int, town: str, name: str):
    publish = Publish(publish_id, town, name)
    return publish


def create_book(book_id: int, amount: int, title: str, volume: str, author: Author, publish: Publish):
    book = Book(book_id, amount, title, volume, author, publish)
    return book


def reserve_book(student: Student, books: List[Book]):
    for book in books:
        book.reserve(Reserve(1, date.today(), student.student_id))  # Бронирование книги


def issue_book(student: Student, books: List[Book]):
    for id, book in enumerate(books):
        book.issue(Issue(id, date.today(), date.today() + timedelta(days=30), student.student_id))  # Получение книги
        reservation_books = book.get_reserve_from_student(student)
        for reserve in reservation_books:
            book.cancel_reservation(reserve)


def extension(student: Student, books: List[Book]):
    for book in books:
        issue_books = book.get_issue_from_student(student)
        for issue in issue_books:
            book.cancel_issue(issue)
            book.issue(
                Issue(issue.issue_id, issue.issue_date, issue.return_date + timedelta(days=14), issue.student_id))
