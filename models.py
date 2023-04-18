from typing import List
from datetime import date, timedelta
from dataclasses import dataclass

''' Факультет '''


class Depart:
    def __init__(self, depart_id: int, phone: str, name: str):
        self.depart_id = depart_id
        self.phone = phone  # телефон
        self.name = name  # наименование

    def __eq__(self, other):
        if isinstance(other, Depart):
            return self.depart_id == other.depart_id
        else:
            return False


''' Автор '''


class Author:
    def __init__(self, author_id: int, fio: str):
        self.author_id = author_id
        self.fio = fio  # ФИО

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.author_id == other.author_id
        else:
            return False


''' Издательство '''


class Publish:
    def __init__(self, publish_id: int, town: str, name: str):
        self.publish_id = publish_id
        self.town = town  # город
        self.name = name  # наименование

    def __eq__(self, other):
        if isinstance(other, Publish):
            return self.publish_id == other.publish_id
        else:
            return False


''' Студент '''


class Student:
    def __init__(self, student_id: int, num: str, fio: str, depart: Depart):
        self.student_id = student_id
        self.num = num  # номер зачетной книжки
        self.fio = fio  # ФИО
        self.depart = depart  # факультет

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        else:
            return False


# Выдача
@dataclass(frozen=True)
class Issue:
    issue_id: int
    issue_date: date
    return_date: date
    student_id: int


# Бронирование
@dataclass(frozen=True)
class Reserve:
    reserve_id: int
    order_date: date
    student_id: int


#  Книга
class Book:
    def __init__(self, book_id: int, amount: int, title: str, annotation: str, author: List[Author], publish: Publish):
        self.book_id = book_id
        self.title = title
        self.annotation = annotation
        self.author = author  # автор
        self.publish = publish  # издательство
        self._amount = amount  # кол-во экземпляров
        self._reserve = set()  # type: Set[Reserve]
        self._issue = set()  # type: Set[Issue]

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.book_id == other.book_id
        else:
            return False

    def reserve(self, obj: Reserve):
        if self.can_get_book():
            self._reserve.add(obj)

    def get_reserve_from_student(self, obj: Student):
        objects = []
        for reserve in self._reserve:
            if reserve.student_id == obj.student_id:
                objects.append(reserve)
        return objects

    def get_issue_from_student(self, obj: Student):
        objects = []
        for issue in self._issue:
            if issue.student_id == obj.student_id:
                objects.append(issue)
        return objects

    def cancel_reservation(self, obj: Reserve):
        if obj in self._reserve:
            self._reserve.remove(obj)

    def cancel_issue(self, obj: Issue):
        if obj in self._issue:
            self._issue.remove(obj)

    def issue(self, obj: Issue):
        if self.can_get_book():
            self._issue.add(obj)
            for r in self._reserve:
                if r.student_id == obj.student_id and r.order_date == obj.issue_date:
                    self.cancel_reservation(r)
                    break

    def remove_issue(self, obj: Issue):
        if obj in self._issue:
            self._issue.remove(obj)

    @property
    def allocated_quantity(self) -> int:
        return len(self._reserve) + len(self._issue)

    @property
    def available_quantity(self) -> int:
        return self._amount - self.allocated_quantity

    def can_get_book(self) -> bool:
        return self._amount - self.allocated_quantity >= 1


def create_student(student_id: int, num: str, fio: str, depart: Depart):
    student = Student(student_id, num, fio, depart)
    return student


def create_depart(depart_id: int, name: str, phone: str):
    depart = Depart(depart_id, phone, name)
    return depart


def create_author(author_id: int, fio: str):
    author = Author(author_id, fio)
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
