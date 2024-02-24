import psycopg2
from base import Database
import os
from dotenv import load_dotenv

load_dotenv()


class Base:
    @staticmethod
    def select(table: str):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column: str, data, table: str):
        if isinstance(data, str):
            query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""

        else:
            query = f"""DELETE FROM {table} WHERE {column} = {data};"""

        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class User(Base):
    def __init__(self, username: str, password: str, gmail: str):
        self.username = username
        while len(password) < 8:
            print("Password kamida 8 ta belgidan inorat bolishi kk:")
            password = input("Password: ")
        self.password = password
        self.gmail = gmail

    def insert(self):
        query = f"""INSERT INTO users(username, password, gmail) VALUES('{self.username}', '{self.password}', '{self.gmail}');"""
        return Database.connect(query, "insert")


class Student(User):
    def __init__(self, username: str, password: str, gmail: str, first_name: str, last_name: str, birt_date,
                 balance: float):
        super().__init__(username, password, gmail)
        self.first_name = first_name
        self.last_name = last_name
        self.birt_date = birt_date
        self.balance = balance

    def insert(self):
        query = f"""INSERT INTO student(username, password, gmail, first_name, last_name, birt_date, balance)
        VALUES('{self.username}', '{self.password}', '{self.gmail}', '{self.first_name}', '{self.last_name}', '{self.birt_date}', '{self.balance}');"""
        return Database.connect(query, "insert")


class Course(Base):
    def __init__(self, name: str, description: str, reyting: float, price: float, continue_time: int):
        self.name = name
        self.description = description
        self.reyting = reyting
        self.price = price
        self.continue_time = continue_time

    def insert(self):
        query = f"""INSERT INTO course(name, description, reyting, price, continue) VALUES('{self.name}', '{self.description}', '{self.reyting}', '{self.price}', '{self.continue_time}');"""
        return Database.connect(query, "insert")


class Mentor(Student):
    def __init__(self, username: str, password: str, gmail: str, first_name: str, last_name: str, birt_date: str,
                 balance: float):
        super().__init__(username, password, gmail, first_name, last_name, birt_date, balance)

    def insert(self):
        query = f"""INSERT INTO mentor(username, password, gmail, first_name, last_name, birt_date, balance)
        VALUES('{self.username}', '{self.password}', '{self.gmail}', '{self.first_name}', '{self.last_name}', '{self.birt_date}', '{self.balance}');"""
        return Database.connect(query, "insert")


class CourseStudent(Base):
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    def insert(self):
        query = f"""INSERT INTO course_student(student_id, course_id) VALUES('{self.student_id}', '{self.course_id}');"""
        return Database.connect(query, "insert")


class Basket(CourseStudent):
    def __init__(self, student_id, course_id):
        super().__init__(student_id, course_id)

    def insert(self):
        query = f"""INSERT INTO basket(student_id, course_id) VALUES('{self.student_id}', '{self.course_id}');"""
        return Database.connect(query, "insert")


class CourseMentor(Base):
    def __init__(self, mentor_id: int, course_id: int):
        self.mentor_id = mentor_id
        self.course_id = course_id

    def insert(self):
        query = f"""INSERT INTO course_mentor(mentor_id, course_id) VALUES('{self.mentor_id}', '{self.course_id}');"""
        return Database.connect(query, "insert")


class CommentCourse(Base):
    def __init__(self, comment_text: str, course_id: int, student_id: int):
        self.comment_text = comment_text
        self.course_id = course_id
        self.student_id = student_id

    def insert(self):
        query = f"""INSERT INTO comment_course(comment_text, course_id, student_id) VALUES('{self.comment_text}', '{self.course_id}'. '{self.student_id}');"""
        return Database.connect(query, "insert")


class Modul(Base):
    def __init__(self, name: str, description: str, continue_time: int, course_id: int):
        self.name = name
        self.description = description
        self.continue_time = continue_time
        self.course_id = course_id

    def insert(self):
        query = f"""INSERT INTO modul(name, description, continue, course_id) VALUES('{self.name}', '{self.description}', '{self.continue_time}', '{self.course_id}');"""
        return Database.connect(query, "insert")


class Lesson(Base):
    def __init__(self, name: str, description: str, modul_id: int):
        self.name = name
        self.description = description
        self.modul_id = modul_id

    def insert(self):
        query = f"""INSERT INTO lesson(name, description, modul_id) VALUES('{self.name}', '{self.description}', '{self.modul_id}');"""
        return Database.connect(query, "insert")


class CommentLesson(Base):
    def __init__(self, comment_text, lesson_id, student_id):
        self.comment_text = comment_text
        self.lesson_id = lesson_id
        self.student_id = student_id

    def insert(self):
        query = f"""INSERT INTO comment_lesson(comment_text, lesson_id, student_id) VALUES('{self.comment_text}', '{self.lesson_id}', '{self.student_id}');"""
        return Database.connect(query, "insert")

# coursestudent = CourseStudent(1,1)
# print(coursestudent.insert())

# mentor = Mentor("me1232", "asdfgghjk", "sfakj@gmail", "Sarvar", "Maxmudov", "2000-12-13", 0.0)
# print(mentor.insert())

# course = Course("python", "best of best", 4.6, 1320000.0, 8)
# print(course.insert())

# student = Student("diyorbek_04", "qwerasdf", "diyorGmail", "Diyorbek", "Maxamadjonov", "2004-03-30", 1200000.0)
# print(student.insert())

# user = User("RN", "87654321", "ravshan@gmail")
# print(user.insert())
