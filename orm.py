import datetime
import logging
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    BigInteger,
    String,
    Date,
    ForeignKey,
    event,
    DateTime
)
from sqlalchemy.orm import mapper, relationship

import models
from models import Depart

logger = logging.getLogger(__name__)

metadata = MetaData()

depart = Table(
    "depart",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("phone", String(255)),
    Column("name", String(255)),
)

author = Table(
    "author",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("fio", String(255)),
)

publish = Table(
    "publish",
    metadata,
    Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("town", String(255)),
    Column("name", String(255)),
)

student = Table(
    "student",
    metadata,
    Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("num", String(255)),
    Column("fio", String(255)),
    Column("depart", Integer, ForeignKey("depart.id")),
)

book = Table(
    "book",
    metadata,
    Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("title", String(255)),
    Column("_amount", Integer, nullable=False),
    Column("author", Integer, ForeignKey("author.id")),
    Column("publish", Integer, ForeignKey("publish.id")),
)

reserve = Table(
    "reserve",
    metadata,
    Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("date_reserve", DateTime(), default=datetime.datetime.now()),
    Column("student", Integer, ForeignKey("student.id"))
)

reserve_book = Table(
    'reserve_book',
    metadata,
    Column('id', BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("book", Integer, ForeignKey("book.id")),
    Column("reserve", Integer, ForeignKey("reserve.id"))
)


def start_mappers():
    mapper(models.Student, student)
    mapper(models.Depart, depart)
    mapper(models.Author, author)
    mapper(models.Publish, publish)
    mapper(models.Book, book)
    mapper(models.Reserve, reserve)
    mapper(models.ReserveBook, reserve_book)
