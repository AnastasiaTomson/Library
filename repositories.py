from abc import ABC, abstractmethod

import models
from models import *


class AbstractRepository(ABC):
    @abstractmethod
    def get_by_id(self, obj_id: int):
        pass

    @abstractmethod
    def get_all(self) -> List:
        pass

    @abstractmethod
    def find(self, **kwargs) -> List:
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def delete(self, obj_id: int):
        pass


class StudentSQLAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def find(self, kwargs) -> Student:
        return self.session.query(models.Student).filter_by(**kwargs).first()

    def get_by_id(self, obj_id: int) -> Student:
        return self.session.query(models.Student).filter_by(id=obj_id).first()

    def get_all(self) -> List[Student]:
        return self.session.query(Student).all()

    def add(self, student: Student):
        self.session.add(student)
        self.session.flush()
        self.session.commit()
        return student

    def delete(self, obj_id: int):
        student = self.get_by_id(obj_id)
        if student is not None:
            self.session.delete(student)


class DepartSQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def find(self, kwargs) -> Depart:
        return self.session.query(models.Depart).filter_by(**kwargs).first()

    def get_by_id(self, obj_id: int) -> Depart:
        return self.session.query(models.Depart).filter_by(id=obj_id).first()

    def get_all(self) -> List[Depart]:
        return self.session.query(Depart).all()

    def add(self, depart: Depart):
        self.session.add(depart)
        self.session.flush()
        self.session.commit()
        return depart

    def delete(self, obj_id: int):
        depart = self.get_by_id(obj_id)
        if depart is not None:
            self.session.delete(depart)


class PublishSQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def find(self, kwargs) -> Publish:
        return self.session.query(models.Publish).filter_by(**kwargs).first()

    def get_by_id(self, obj_id: int) -> Publish:
        return self.session.query(models.Publish).filter_by(id=obj_id).first()

    def get_all(self) -> List[Publish]:
        return self.session.query(Publish).all()

    def add(self, publish: Publish):
        self.session.add(publish)
        self.session.flush()
        self.session.commit()
        return publish

    def delete(self, obj_id: int):
        publish = self.get_by_id(obj_id)
        if publish is not None:
            self.session.delete(publish)


class AuthorSQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def find(self, kwargs) -> Author:
        return self.session.query(models.Author).filter_by(**kwargs).first()

    def get_by_id(self, obj_id: int) -> Author:
        return self.session.query(models.Author).filter_by(id=obj_id).first()

    def get_all(self) -> List[Author]:
        return self.session.query(Author).all()

    def add(self, author: Author):
        self.session.add(author)
        self.session.flush()
        self.session.commit()
        return author

    def delete(self, obj_id: int):
        author = self.get_by_id(obj_id)
        if author is not None:
            self.session.delete(author)


class BookSQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def find(self, kwargs) -> Book:
        return self.session.query(models.Book).filter_by(**kwargs).first()

    def get_by_id(self, obj_id: int) -> Book:
        return self.session.query(models.Book).filter_by(id=obj_id).first()

    def get_all(self) -> List[Book]:
        return self.session.query(Book).all()

    def add(self, book: Book):
        self.session.add(book)
        self.session.flush()
        self.session.commit()
        return book

    def delete(self, obj_id: int):
        book = self.get_by_id(obj_id)
        if book is not None:
            self.session.delete(book)


class ReserveSQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def find(self, kwargs) -> Reserve:
        return self.session.query(models.Reserve).filter_by(**kwargs).first()

    def get_by_id(self, obj_id: int) -> Reserve:
        return self.session.query(models.Reserve).filter_by(id=obj_id).first()

    def get_all(self) -> List[Reserve]:
        return self.session.query(Reserve).all()

    def add(self, reserve: Reserve):
        self.session.add(reserve)
        self.session.flush()
        self.session.commit()
        return reserve

    def delete(self, obj_id: int):
        reserve = self.get_by_id(obj_id)
        if reserve is not None:
            self.session.delete(reserve)

    def reserve_book(self, reserve: Reserve, books: List[Book]):
        for book in books:
            r_book = ReserveBook(book.id, reserve.id)
            self.session.add(r_book)
            self.session.commit()
