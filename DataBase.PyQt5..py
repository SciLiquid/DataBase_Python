from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Librarian(Base):

    __tablename__ = 'Librarian'

    ID_librarian = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    Years_of_work = Column(Integer)
    ID_worker = Column(Integer, ForeignKey("workers.id"))
    ID_account = Column(Integer,ForeignKey("account.ID_ER"))
    ID_book = Column(Integer, ForeignKey('Book.ID_book'))

    def __repr__(self):
        return f'{self.ID_librarian} {self.Years_of_work} {self.ID_worker} {self.ID_account} {self.ID_book}'


class Book(Base):

    __tablename__ = "Book"

    ID_book = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    Auther = Column(String(128))
    Title = Column(String(128))
    Tom = Column(Integer)
    Subject_field = Column(String(128))
    Publishing_year = Column(Integer)
    Number_of_samples = Column(Integer)

    def __repr__(self):
        return f'{self.ID_book} {self.Auther} {self.Title} {self.Tom} {self.Subject_field} {self.Publishing_year} {self.Number_of_samples}'

class Student(Base):

    __tablename__ = 'Student'

    Student_card = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    Group = Column(String(128))
    Course = Column(Integer)

    def __repr__(self):
        return f'{self.Student_card} {self.Group} {self.Course}'


class Account(Base):
    __tablename__ = 'account'

    ID_ER = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    User_name = Column(String(128))
    Password = Column(Integer)

    def __repr__(self):
        return f'{self.ID_ER} {self.User_name} {self.Password}'


class workers(Base):
    __tablename__ = 'workers'

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    salary = Column(Integer)
    NS = Column(String(128))
    job = Column(String(128))
    def __repr__(self):
        return f'{self.id} {self.salary} {self.NS} {self.job}'


class Tail(Base):
    __tablename__ = 'Tail'

    ID = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    ID_book = Column(Integer, ForeignKey("Book.ID_book"))
    ID_student = Column(Integer, ForeignKey("Student.Student_card"))


def __repr__(self):
    return f'{self.ID} {self.ID_book} {self.ID_student}'

engine = create_engine('sqlite:///Table_Lib',echo=True)

Base.metadata.create_all(engine)

get_session = sessionmaker(engine, autocommit=False)

session=get_session()

session=get_session()

boobs=session.query(Book).all()
print(boobs)


print("Что это за проект?")

print('Добавить сюда')