import requests
from database_operations import DataBaseOperations
from io_interface import IOInterface
from back_up_data import BackUpData
from tables_filler import TablesFiller


def main():
    hb_students_api = "https://hackbulgaria.com/api/students/"
    students_info = requests.get(hb_students_api).json()

    BackUpData.save_data_in_file("hb_students_api.json", students_info)
    data = BackUpData.read_data_from_file("hb_students_api.json")

    students_db = DataBaseOperations("hackbulgaria_students.db")
    TablesFiller.connect_database(students_db)
    TablesFiller.create_students_table(students_db)
    TablesFiller.create_courses_table(students_db)
    TablesFiller.create_students_to_cources_table(students_db)

    TablesFiller.fill_students(students_db, data)
    TablesFiller.fill_courses(students_db, data)
    TablesFiller.fill_students_to_courses(students_db, data)

    IOInterface.print_commands()
    IOInterface.command_input(students_db)



if __name__ == '__main__':
    main()
