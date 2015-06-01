import sqlite3


class DataBaseOperations:

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def connect_database(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def disconnect_database(self):
        self.connection.close()

    def create_students_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY,
            student_name TEXT,
            student_github TEXT,
            student_available)""")

        self.connection.commit()

    def delete_students_table(self):
        self.cursor.execute("""
            DELETE FROM students
            """)

        self.connection.commit()

    def create_courses_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS courses(
            course_id INTEGER PRIMARY KEY,
            course_name TEXT)""")

        self.connection.commit()

    def delete_courses_table(self):
        self.cursor.execute("""
            DELETE FROM courses
            """)

        self.connection.commit()

    def create_students_to_cources_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS students_to_courses(
            student_id INTEGER,
            course_id INTEGER,
            student_group INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(course_id) REFERENCES courses(course_id))""")

        self.connection.commit()

    def delete_junction_table(self):
        self.cursor.execute("""
            DELETE FROM students_to_courses
            """)

        self.connection.commit()

    def add_student(self, name, github, available):
        self.cursor.execute("""INSERT INTO students(student_name,
            student_github, student_available)
            VALUES(?,?,?)""", (name, github, available))

        self.connection.commit()

    def add_course(self, name):
        self.cursor.execute("""INSERT INTO courses(course_name)
            VALUES(?)""", (name,))

        self.connection.commit()

    def add_students_to_courses(self, student_id, course_id, student_group):
        self.cursor.execute("""INSERT INTO students_to_courses
            (student_id, course_id, student_group)VALUES(?,?,?)""",
                            (student_id, course_id, student_group))

        self.connection.commit()

    def get_course_id(self, course_name):
        course = self.cursor.execute("""SELECT course_id FROM courses
            WHERE course_name = ?""", (course_name,))

        return course.fetchone()[0]

    def get_course_name(self, course_id):
        name = self.cursor.execute("""SELECT course_name FROM courses
            WHERE course_id = ?""", (course_id,))

        return name.fetchone[0]

    def get_student_id(self, student_name):
        student_name = self.cursor.execute("""
            SELECT student_id FROM students WHERE student_name = ? """,
                                           (student_name,))

        return student_name.fetchone()[0]

    def get_all_students(self):
        self.cursor.execute("""
            SELECT student_id, student_name, student_github
            FROM Students""")

        all_students = self.cursor.fetchall()

        return all_students

    def get_all_courses(self):
        self.cursor.execute("""SELECT course_id, course_name FROM courses """)

        all_courses = self.cursor.fetchall()

        return all_courses

    def get_students_courses(self):
        get_students_and_courses = """SELECT students.student_id,
            student_name AS s_name, course_name AS c_name
            FROM students, courses
            JOIN students_to_courses
            ON students_to_courses.student_id = students.student_id
            AND students_to_courses.course_id = courses.course_id
            ORDER BY students.student_id ASC"""

        relation = self.cursor.execute(get_students_and_courses)

        return relation.fetchall()

    def get_students_with_most_courses(self):
        command = """SELECT student_name
            FROM students AS S
            INNER JOIN Students_to_Courses AS StoC
            ON S.student_id = StoC.student_id
            GROUP BY StoC.student_id
            ORDER BY COUNT(StoC.student_id) DESC
            LIMIT 5 """

        students_with_most_courses = self.cursor.execute(command)

        return students_with_most_courses.fetchall()
