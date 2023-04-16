from abc import ABC, abstractmethod
from models import *


class AbstractRepository(ABC):
    @abstractmethod
    def get_by_id(self, obj_id: int):
        pass

    @abstractmethod
    def get_all(self) -> List:
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def delete(self, obj_id: int):
        pass


class StudentLocalRepository(AbstractRepository):
    def __init__(self):
        self.students: List[Student] = []

    def get_by_id(self, obj_id: int):
        for student in self.students:
            if student.student_id == obj_id:
                return student
        return None

    def get_all(self):
        return self.students

    def add(self, student: Student):
        self.students.append(student)

    def delete(self, obj_id: int):
        student = self.get_by_id(obj_id)
        if student is not None:
            self.students.remove(student)


class BookLocalRepository(AbstractRepository):
    def __init__(self):
        self.books: List[Book] = []

    def get_by_id(self, obj_id: int):
        for book in self.books:
            if book.book_id == obj_id:
                return book
        return None

    def get_all(self):
        return self.books

    def add(self, book: Book):
        self.books.append(book)

    def delete(self, obj_id: int):
        book = self.get_by_id(obj_id)
        if book is not None:
            self.books.remove(book)


class AuthorLocalRepository(AbstractRepository):
    def __init__(self):
        self.authors: List[Author] = []

    def get_by_id(self, obj_id: int):
        for author in self.authors:
            if author.author_id == obj_id:
                return author
        return None

    def get_all(self):
        return self.authors

    def add(self, author: Author):
        self.authors.append(author)

    def delete(self, obj_id: int):
        author = self.get_by_id(obj_id)
        if author is not None:
            self.authors.remove(author)


class PublishLocalRepository(AbstractRepository):
    def __init__(self):
        self.publishes: List[Publish] = []

    def get_by_id(self, obj_id: int):
        for publish in self.publishes:
            if publish.publish_id == obj_id:
                return publish
        return None

    def get_all(self):
        return self.publishes

    def add(self, publish: Publish):
        self.publishes.append(publish)

    def delete(self, obj_id: int):
        publish = self.get_by_id(obj_id)
        if publish is not None:
            self.publishes.remove(publish)


class DepartLocalRepository(AbstractRepository):
    def __init__(self):
        self.departs: List[Depart] = []

    def get_by_id(self, obj_id: int):
        for depart in self.departs:
            if depart.depart_id == obj_id:
                return depart
        return None

    def get_all(self):
        return self.departs

    def add(self, depart: Depart):
        self.departs.append(depart)

    def delete(self, obj_id: int):
        depart = self.get_by_id(obj_id)
        if depart is not None:
            self.departs.remove(depart)


class ReserveLocalRepository(AbstractRepository):
    def __init__(self):
        self.reserves: List[Reserve] = []

    def get_by_id(self, obj_id: int):
        for reserve in self.reserves:
            if reserve.reserve_id == obj_id:
                return reserve
        return None

    def get_all(self):
        return self.reserves

    def add(self, reserve: Reserve):
        self.reserves.append(reserve)

    def delete(self, obj_id: int):
        reserve = self.get_by_id(obj_id)
        if reserve is not None:
            self.reserves.remove(reserve)


class IssueLocalRepository(AbstractRepository):
    def __init__(self):
        self.issues: List[Issue] = []

    def get_by_id(self, obj_id: int):
        for issue in self.issues:
            if issue.issue_id == obj_id:
                return issue
        return None

    def get_all(self):
        return self.issues

    def add(self, issue: Issue):
        self.issues.append(issue)

    def delete(self, obj_id: int):
        issue = self.get_by_id(obj_id)
        if issue is not None:
            self.issues.remove(issue)

