from base import Database


def insert():
    user = f"""CREATE TABLE users(
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(25),
        password VARCHAR(25),
        gmail VARCHAR(30),
        last_update TIMESTAMP DEFAULT now());"""

    student = f"""CREATE TABLE student(
        student_id SERIAL PRIMARY KEY,
        username VARCHAR(25),
        password VARCHAR(25),
        gmail VARCHAR(30),
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        birt_date DATE,
        balance FLOAT,
        last_update TIMESTAMP DEFAULT now());"""

    course = f"""CREATE TABLE course(
        course_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        description TEXT,
        reyting FLOAT,
        price FLOAT,
        continue SMALLINT,
        last_update TIMESTAMP DEFAULT now());"""

    mentor = f"""CREATE TABLE mentor(
        mentor_id SERIAL PRIMARY KEY,
        username VARCHAR(20),
        password VARCHAR(20),
        gmail VARCHAR(30),
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        birt_date DATE,
        balance FLOAT,
        last_update TIMESTAMP DEFAULT now());"""

    course_student = f"""CREATE TABLE course_student(
        course_student_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES student(student_id),
        course_id INT REFERENCES course(course_id),
        last_update TIMESTAMP DEFAULT now());"""

    basket = f"""CREATE TABLE basket(
            basket_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id),
            last_update TIMESTAMP DEFAULT now());"""

    course_mentor = f"""CREATE TABLE course_mentor(
        course_mentor_id SERIAL PRIMARY KEY,
        mentor_id INT REFERENCES mentor(mentor_id),
        course_id INT REFERENCES course(course_id),
        last_update TIMESTAMP DEFAULT now());"""

    comment_course = f"""CREATE TABLE comment_course(
        comment_course_id SERIAL PRIMARY KEY,
        comment_text TEXT,
        course_id INT REFERENCES course(course_id),
        student_id INT REFERENCES student(student_id),
        last_update TIMESTAMP DEFAULT now());"""

    modul = f"""CREATE TABLE modul(
        modul_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        description TEXT,
        continue SMALLINT,
        course_id INT REFERENCES course(course_id),
        last_update TIMESTAMP DEFAULT now());"""

    lesson = f"""CREATE TABLE lesson(
        lesson_id SERIAL PRIMARY KEY,
        name VARCHAR(15),
        description TEXT,
        modul_id INT REFERENCES modul(modul_id),
        last_update TIMESTAMP DEFAULT now());"""

    comment_lesson = f"""CREATE TABLE comment_lesson(
        comment_lesson_id SERIAL PRIMARY KEY,
        comment_text TEXT,
        lesson_id INT REFERENCES lesson(lesson_id),
        student_id INT REFERENCES student(student_id),
        last_update TIMESTAMP DEFAULT now());"""

    data = {
        "user": user,
        "student": student,
        "course": course,
        "mentor": mentor,
        "course_student": course_student,
        "basket": basket,
        "course_mentor": course_mentor,
        "comment_course": comment_course,
        "modul": modul,
        "lesson": lesson,
        "comment_lesson": comment_lesson
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], 'create')}")


# if __name__ == "__main__":
#     insert()