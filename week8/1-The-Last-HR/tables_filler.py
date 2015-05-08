class TablesFiller:

    @staticmethod
    def connect_database(database):
        database.connect_database()
        print("We have connection with the database")

    @staticmethod
    def disconnect_database(company):
        company.disconnect_database()
        print("Database disconnected")

    @staticmethod
    def create_students_table(company):
        company.create_students_table()
        print ("Students table created")

    @staticmethod
    def create_courses_table(company):
        company.create_courses_table()
        print ("Courses table created")

    @staticmethod
    def create_students_to_cources_table(company):
        company.create_students_to_cources_table()
        print ("Students to Courses table created")

    @staticmethod
    def fill_students(database, all_students):
        database.delete_students_table()

        for index in range(len(all_students)):
            student_name = all_students[index]["name"]
            student_github = all_students[index]["github"]
            student_available = all_students[index]["available"]

            database.add_student(
                student_name, student_github, student_available)

        print ("Students filled")

    @staticmethod
    def fill_courses(database, all_students):
        courses = set()

        for item in all_students:
            for course in item["courses"]:
                courses.add(course["name"])

        database.delete_courses_table()

        for name in courses:
            database.add_course(name)

        print ("Courses filled")

    @staticmethod
    def fill_students_to_courses(database, data):

        database.delete_junction_table()

        for item in data:
            student_id = database.get_student_id(item["name"])
            for course in item["courses"]:
                course_id = database.get_course_id(course["name"])
                student_group = course["group"]
                database.add_students_to_courses(
                    student_id, course_id, student_group)

        print ("Students to Courses filled")
