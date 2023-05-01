import datetime

import models
import repositories
from models import *
from datetime import date, timedelta
import pytest
from sqlalchemy import create_engine, BigInteger, text, insert, select
from sqlalchemy.orm import sessionmaker, query, Session
import orm

engine = create_engine("sqlite:///library.db")
session = Session(autoflush=False, bind=engine)

orm.metadata.create_all(bind=engine)
orm.start_mappers()


def test_student_repository_can_save():
    student_repository = repositories.StudentSQLAlchemyRepository(session)
    depart_repository = repositories.DepartSQLAlchemyRepository(session)

    depart = depart_repository.find({'phone': "+7(000)777-77-77", 'name': "Гриффиндор"})
    if not depart:
        depart = Depart("+7(000)777-77-77", "Гриффиндор")
        depart_repository.add(depart)
    student = student_repository.find({'num': "11111", 'fio': 'Петров Петр Петрович', 'depart': depart.id})
    if not student:
        student = models.Student('11111', 'Петров Петр Петрович', depart.id)
        student_repository.add(student)
    assert student.fio == 'Петров Петр Петрович'


def test_book_repository_can_save():
    book_repository = repositories.BookSQLAlchemyRepository(session)
    publish_repository = repositories.PublishSQLAlchemyRepository(session)
    author_repository = repositories.AuthorSQLAlchemyRepository(session)

    publish = publish_repository.find({'town': "Москва", 'name': "Махаон"})
    if not publish:
        publish = Publish("Москва", "Махаон")
        publish_repository.add(publish)

    author = author_repository.find({'fio': "Александр Сергеевич Пушкин"})
    if not author:
        author = models.Author("Александр Сергеевич Пушкин")
        author_repository.add(author)

    book = book_repository.find({'title': "Евгений Онегин"})
    if not book:
        book = models.Book(17, "Евгений Онегин", author.id, publish.id)
        book_repository.add(book)

    assert book.title == "Евгений Онегин"


def test_reserve_book_repository_can_save():
    book_repository = repositories.BookSQLAlchemyRepository(session)
    publish_repository = repositories.PublishSQLAlchemyRepository(session)
    author_repository = repositories.AuthorSQLAlchemyRepository(session)
    reserve_book_repository = repositories.ReserveSQLAlchemyRepository(session)
    student_repository = repositories.StudentSQLAlchemyRepository(session)
    depart_repository = repositories.DepartSQLAlchemyRepository(session)

    depart = depart_repository.find({'phone': "+7(000)777-77-77", 'name': "Гриффиндор"})
    if not depart:
        depart = Depart("+7(000)777-77-77", "Гриффиндор")
        depart_repository.add(depart)

    student = student_repository.find({'num': "11111", 'fio': 'Петров Петр Петрович', 'depart': depart.id})
    if not student:
        student = models.Student('11111', 'Петров Петр Петрович', depart.id)
        student_repository.add(student)

    publish = publish_repository.find({'town': "Москва", 'name': "Махаон"})
    if not publish:
        publish = Publish("Москва", "Махаон")
        publish_repository.add(publish)

    author = author_repository.find({'fio': "Александр Сергеевич Пушкин"})
    if not author:
        author = models.Author("Александр Сергеевич Пушкин")
        author_repository.add(author)

    book1 = book_repository.find({'title': "Евгений Онегин"})
    if not book1:
        book1 = models.Book(17, "Евгений Онегин", author.id, publish.id)
        book_repository.add(book1)

    book2 = book_repository.find({'title': "Борис Годунов"})
    if not book2:
        book2 = models.Book(5, "Борис Годунов", author.id, publish.id)
        book_repository.add(book2)

    reserve = reserve_book_repository.find({'date_reserve': datetime.datetime.today()})
    if not reserve:
        reserve = models.Reserve(student=student.id)
        reserve_book_repository.add(reserve)
        reserve_book_repository.reserve_book(reserve, [book1, book2])
    assert reserve.date_reserve.date() == datetime.datetime.today().date()
