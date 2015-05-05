import sqlite3


class CompanyManager:

    MONTHS = 12

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def connect_database(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def disconnect_database(self):
        self.connection.close()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY,
                name TEXT,
                montly_salary INTEGER,
                yearly_bonus INTEGER,
                position TEXT)
            """)
        self.connection.commit()

    def fill_table(self):
        self.cursor.execute('''INSERT INTO employees(name, montly_salary, yearly_bonus, position)
                      VALUES(?,?,?,?)''',
                            ("Ivan Ivanov", 5000, 10000, "Software Developer"))

        self.cursor.execute('''INSERT INTO employees(name, montly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''',
                            ("Rado Rado", 500, 0, "Technical Support Intern"))

        self.cursor.execute('''INSERT INTO employees(name, montly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', ("Ivo Ivo", 10000, 100000, "CEO"))

        self.cursor.execute('''INSERT INTO employees(name, montly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''',
                            ("Petar Petrov", 3000, 1000, "Marketing Manager"))

        self.cursor.execute('''INSERT INTO employees(name, montly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', ("Maria Georgieva", 8000, 10000, "COO"))

        self.connection.commit()

    def list_employees(self):
        return self.cursor.execute("""
            SELECT id, name, position FROM employees""")

    def monthly_spending(self):
        spendings = self.cursor.execute("SELECT montly_salary FROM employees")

        amount = 0
        for money in spendings:
            amount += int(money[0])

        return amount

    def yearly_spending(self):
        bonuses = self.cursor.execute("SELECT yearly_bonus FROM employees")

        amount = 0
        for money in bonuses:
            amount += int(money[0])

        amount += self.monthly_spending() * CompanyManager.MONTHS
        return amount

    def add_employee(self, name, montly_salary, yearly_bonus, position):
        self.cursor.execute("""
            INSERT INTO employees(name, montly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)""", (str(name), montly_salary,
                                    yearly_bonus, str(position)))

        self.connection.commit()

    def delete_employee(self, employee_id):
        employee = self.cursor.execute("""
            SELECT * FROM employees WHERE id = ? """, (employee_id))

        name = employee.fetchone()[1]

        self.cursor.execute("""
            DELETE FROM employees WHERE id = ? """, (employee_id))

        self.connection.commit()

        return name

    def update_employee(self, employee_id, name, montly_salary,
                        yearly_bonus, position):

        self.cursor.execute("""
            UPDATE employees SET
            name = ?, montly_salary = ?, yearly_bonus= ?, position = ?
            WHERE id = ? """, (name, montly_salary,
                               yearly_bonus, position, employee_id))

        self.connection.commit()
