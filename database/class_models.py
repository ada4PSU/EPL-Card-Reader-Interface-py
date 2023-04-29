import datetime
from typing import Optional
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

# Replaced depreciated 'Base = declarative_base()'
class Base(DeclarativeBase):
    pass

# User Table:
	# Primary Key: ID Number
	# First Name
	# Last Name
    # Email
    # Role

class User(Base):
    __tablename__ = "user"
    # Declarative Form, prefered as of SQLAlchemy 2.0
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    email: Mapped[str]
    role: Mapped[str]
    # List of machines the user is trained on
    #machines: Mapped[Optional[list["UserMachine"]]] = relationship(back_populates="user.id")
    #trainings: Mapped[Optional[list["trainings"]]] = relationship(back_populates="user")

    # Imperative Form, legacy since SQLAlchemy 1.4, may need some tweaking
    #id = Column(Integer, primary_key=True)
    #firstname = Column(String)
    #lastname = Column(String)
    #email = Column(String)
    #machines = relationship('Machine', secondary=students_machines, backref=backref('students', lazy='dynamic'))
    #trainings = relationship.back_populates('StudentMachine', lazy='dynamic')
    
    def __init__(self, id, fname, lname, email, role):
        self.id = id
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.role = role
    
    def __repr__(self):
        return f"{self.firstname} {self.lastname}"
  
class Machine(Base):
    __tablename__ = "machine"
    # Declarative Form, prefered as of SQLAlchemy 2.0
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    # List of Users that are trained on this machine
    #trainings: Mapped[list["UserMachine"]] = relationship(back_populates="machine.id")

    # Imperative Form, legacy since SQLAlchemy 1.4
    #id = Column(Integer, primary_key=True)
    #name = Column(String)
    #trainings = relationship('StudentMachine', backref='machine', lazy='dynamic')
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return self.name
"""    
class UserMachine(Base):
    __tablename__ = "usermachine"
    # Declarative Form, prefered as of SQLAlchemy 2.0
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    machine_id: Mapped[int] = mapped_column(ForeignKey("machine.id"))
    last_trained: Mapped[datetime.datetime]

    # Imperative Form, legacy since SQLAlchemy 1.4
    #id = Column(Integer, primary_key=True)
    #student_id = Column(Integer, ForeignKey('student.id'))
    #machine_id = Column(Integer, ForeignKey('machine.id'))
    #last_trained = Column(datetime.datetime)
    
    def __init__(self, student, machine, date):
        self.student = student
        self.machine = machine
        self.last_trained = date
    
    def __repr__(self):
        return f"{self.student} was last trained on {self.machine} on {self.last_trained}"
    
# Define the association table for the many-to-many relationship between Student and Machine
# This is equivalent to defining the UserMachine class
#students_machines = Table('students_machines',
    #Column('student_id', Integer, ForeignKey('student.id'), primary_key=True),
    #Column('machine_id', Integer, ForeignKey('machine.id'), primary_key=True)
#)

#training = StudentMachine(student=student1, machine=machine2, date=datetime.now())
#student1.trainings.append(training)
#machine2.trainings.append(training)
"""