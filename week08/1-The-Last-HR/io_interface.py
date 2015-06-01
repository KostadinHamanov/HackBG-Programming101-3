class IOInterface:

    @staticmethod
    def connect_database(database):
        database.connect_database()
        print("We have connection with the database")

    @staticmethod
    def disconnect_database(company):
        company.disconnect_database()
        print("Database disconnected")

    @staticmethod
    def print_commands():
        print("-" * 25)
        print ("Please choose a command:")
        print ("all_students")
        print ("all_courses")
        print ("students_courses")
        print ("students_with_most_courses")
        print ("menu")
        print ("exit")
        print("-" * 25)

    @staticmethod
    def command_input(database):
        command = input("command>")

        while command != "exit":
            IOInterface.choose_command(database, command)
            command = input("command>")

    @staticmethod
    def choose_command(company, command):
        if command == "all_students":
            IOInterface.list_all_students(company)
        elif command == "all_courses":
            IOInterface.list_all_courses(company)
        elif command == "students_courses":
            IOInterface.list_students_courses(company)
        elif command == "students_with_most_courses":
            IOInterface.list_students_with_most_courses(company)
        elif command == "menu":
            IOInterface.print_commands()
        else:
            print("Invalid command")

    @staticmethod
    def list_all_students(company):
        students = company.get_all_students()

        for student in students:
            print("{} - {} - {}". format(
                student[0], student[1], student[2]))

    @staticmethod
    def list_all_courses(company):
        courses = company.get_all_courses()

        for course in courses:
            print ("{} - {}". format(
                course[0], course[1]))

    @staticmethod
    def list_students_courses(company):
        students_courses = company.get_students_courses()

        for student_course in students_courses:
            print("{} - {} - {}". format(
                student_course[0], student_course[1], student_course[2]))

    @staticmethod
    def list_students_with_most_courses(company):
        students = company.get_students_with_most_courses()

        for student in students:
            print("{}" .format(student[0]))
