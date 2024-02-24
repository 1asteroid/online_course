import classes


def insertion_comment_lesson():
    comment = input("\t\tLesson haqida fikringiz: ")
    student_id = int(input("\t\t Student id(student tableda yaratilgan): "))
    lesson_id = int(input("\t\t Lesson id(lesson tableda yaratilgan): "))
    comment_lesson = classes.CommentLesson(comment, lesson_id, student_id)
    return comment_lesson.insert()


def insertion_lesson():
    name = input("\t\tLesson name: ")
    description = input("\t\tLesson description: ")
    modul_id = int(input("\t\tLesson tegishli bolgan modul id: "))
    lesson = classes.Lesson(name, description, modul_id)
    return lesson.insert()


def insertion_modul():
    name = input("\t\tModul name: ")
    description = input("\t\tModul description: ")
    continue_time = int(input("\t\tModulning davomiyligi(necha oydan iborat): "))
    course_id = int(input("\t\tModul tegishli bolgan course id: "))
    modul = classes.Modul(name, description, continue_time, course_id)
    return modul.insert()


def insertion_comment_course():
    comment = input("\t\tCourse haqida fikringiz: ")
    student_id = int(input("\t\t Student id(student tableda yaratilgan): "))
    course_id = int(input("\t\t Course id(course tableda yaratilgan): "))
    comment_course = classes.CommentCourse(comment, course_id, student_id)
    return comment_course.insert()


def insertion_course_mentor():
    mentor_id = int(input("\t\t Mentor id(mentor tableda yaratilgan): "))
    course_id = int(input("\t\t Course id(course tableda yaratilgan): "))
    coursementor = classes.CourseMentor(mentor_id, course_id)
    return coursementor.insert()


def insertion_basket():
    student_id = int(input("\t\t Student id(student tableda yaratilgan): "))
    course_id = int(input("\t\t Course id(course tableda yaratilgan): "))
    basket = classes.Basket(student_id, course_id)
    return basket.insert()


def insertion_course_student():
    student_id = int(input("\t\t Student id(student tableda yaratilgan): "))
    course_id = int(input("\t\t Course id(course tableda yaratilgan): "))
    coursestudent = classes.CourseStudent(student_id, course_id)
    return coursestudent.insert()


def insertion_mentor():
    username = input("\t\t Username: ")
    password = input("\t\t Password: ")
    gmail = input("\t\t gmail: ")
    first_name = input("\t\t first name: ")
    last_name = input("\t\t last name: ")
    birt_date = input("\t\t Birtday date example(2004-03-30): ")
    balance = float(input("\t\t Balance: "))
    mentor = classes.Mentor(username, password, gmail, first_name, last_name, birt_date, balance)
    return mentor.insert()


def insertion_course():
    name = input("\t\tname: ")
    description = input("\t\tdescription: ")
    reyting = float(input("\t\treyting(float): "))
    price = float(input("\t\tprice(float): "))
    continue_time = int(input("\t\tDavomiyligi (necha oy davom etadi): "))
    course = classes.Course(name, description, reyting, price, continue_time)
    return course.insert()


def insertion_student():
    username = input("\t\t Username: ")
    password = input("\t\t Password: ")
    gmail = input("\t\t gmail: ")
    first_name = input("\t\t first name: ")
    last_name = input("\t\t last name: ")
    birt_date = input("\t\t Birtday date example(2004-03-30): ")
    balance = float(input("\t\t Balance: "))
    student = classes.Student(username, password, gmail, first_name, last_name, birt_date, balance)
    return student.insert()


def insertion_user():
    username = input("\t\t Username: ")
    password = input("\t\t Password: ")
    gmail = input("\t\t gmail: ")
    user = classes.User(username, password, gmail)
    return user.insert()


def insertion(table):
    if table == "users":
        return insertion_user()

    elif table == "student":
        return insertion_student()

    elif table == "course":
        return insertion_course()

    elif table == "mentor":
        return insertion_mentor()

    elif table == "course_student":
        return insertion_course_student()

    elif table == "basket":
        return insertion_basket()

    elif table == "course_mentor":
        return insertion_course_mentor()

    elif table == "comment_course":
        return insertion_comment_course()

    elif table == "course_student":
        return insertion_modul()

    elif table == "course_lesson":
        return insertion_lesson()

    elif table == "comment_lesson":
        return insertion_comment_lesson()

    else:
        return "Aniqlanmagan buyruq"


def task(table_name: str):
    choose = input(f"""
    <--- Qaysi birini tanlaysiz??? --->
        1. SELECT
        2. INSERT
        3. DELETE
        4. UPDATE
        
        0. back
            =>> """)
    if choose == "1":
        print(f"\n\t\t <--- {table_name} --->\n")
        for i in classes.Base.select(table_name):
            print(i)
        return task(table_name)

    elif choose == "2":
        print(insertion(table_name))
        return task(table_name)

    elif choose == "3":
        column = input("\t\t Column name: ")
        data = input("\t\t o'chirmoqchi bo'lganizni xususiyati(kiritgan Column boyicha): ")
        print(classes.Base.delete(column, data, table_name))
        return task(table_name)

    elif choose == "4":
        print("\t\t<--- Update qilishning turli usullari bor.--->")
        query = input("\t\t To'liq sorov kiriting: ")
        print(classes.Base.update(query))
        return task(table_name)

    elif choose == "0":
        return main()

    else:
        print("\t\t<--- Bunday buyruq mavjud emas. Iltimos tekshirib qaytadan kiriting!!! --->")
        return task(table_name)


def main():
    table = input(f"""
    <--- Qaysi tableni tanlaysiz??? --->
        1. user
        2. student
        3. course
        4. mentor
        5. course_student
        6. basket
        7. course_mentor
        8. comment_course
        9. modul
        10. lesson
        11. comment_lesson
         =>> """)

    data = {
        "1": "users",
        "2": "student",
        "3": "course",
        "4": "mentor",
        "5": "course_student",
        "6": "basket",
        "7": "course_mentor",
        "8": "comment_course",
        "9": "modul",
        "10": "lesson",
        "11": "comment_lesson"
    }
    if table in data.keys():
        task(data[table])

    else:
        print("\t\t<-- Bunday buyruq mavjud emas!!! -->")
        return main()


if __name__ == "__main__":
    main()
