from manage_company import CompanyManager


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
    def create_table(company):
        company.create_table()
        print ("Table created")

    @staticmethod
    def fill_table(company):
        company.fill_table()
        print("Table filled")

    @staticmethod
    def print_commands():
        print("-" * 25)
        print ("Please choose a command:")
        print ("list_employees")
        print ("monthly_spending")
        print ("yearly_spending")
        print ("add_employee")
        print ("delete_employee")
        print ("update_employee")
        print ("exit")
        print("-" * 25)

    @staticmethod
    def read_command(company, command):
        # IOInterface.connect_database(company)
        if command == "list_employees":
            IOInterface.list_employees(company)
        elif command == "monthly_spending":
            IOInterface.monthly_spending(company)
        elif command == "yearly_spending":
            IOInterface.yearly_spending(company)
        elif command == "add_employee":
            IOInterface.add_employee(company)
        elif command == "delete_employee":
            IOInterface.delete_employee(company)
        elif command == "update_employee":
            IOInterface.update_employee(company)
        else:
            print("Invalid command")

    @staticmethod
    def list_employees(company):
        employees = company.list_employees()

        for employee in employees:
            print("{} - {} - {}". format(
                employee[0], employee[1], employee[2]))

    @staticmethod
    def monthly_spending(company):
        amount = company.monthly_spending()
        print ("The company is spending ${} every month!". format(amount))

    @staticmethod
    def yearly_spending(company):
        amount = company.yearly_spending()
        print ("The company is spending ${} every year!". format(amount))

    @staticmethod
    def add_employee(company):
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        company.add_employee(name, monthly_salary, yearly_bonus, position)

    @staticmethod
    def delete_employee(company):
        employee_id = input('id>')
        employee_to_delete = company.delete_employee(employee_id)
        print("{} was deleted" . format(employee_to_delete))

    @staticmethod
    def update_employee(company):
        employee_id = input('id>')
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        company.update_employee(employee_id, name,
                                monthly_salary, yearly_bonus, position)

        print ("Updating successful")
