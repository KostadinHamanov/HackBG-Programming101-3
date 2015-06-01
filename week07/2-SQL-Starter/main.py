from manage_company import CompanyManager
from io_interface import IOInterface


def main():
    my_company = CompanyManager("company.db")

    IOInterface.connect_database(my_company)
    IOInterface.create_table(my_company)
    # IOInterface.fill_table(my_company)

    IOInterface.print_commands()

    command = input('command>')

    while command != "exit":
        IOInterface.read_command(my_company, command)
        command = input('command>')

    IOInterface.disconnect_database(my_company)

if __name__ == '__main__':
    main()
