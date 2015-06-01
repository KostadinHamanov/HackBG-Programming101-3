from cinema_database import CinemaDatabase
from hall import Hall
from settings import DB_NAME


class CommandIO:

    @staticmethod
    def start():
        database = CinemaDatabase(DB_NAME)
        database.prepare()
        CommandIO.welcome()
        CommandIO.menu()
        CommandIO.input_command(database)

    @staticmethod
    def welcome():
        print()
        print('-' * 44)
        print("Welcome to CINEMA RESERVATION SYSTEM. Enjoy!")
        print('-' * 44)

    @staticmethod
    def menu():
        print()
        print("Please choose a command:")
        print()
        print("show_movies")
        print("show_movie_projections")
        print("make_reservation")
        print("cancel_reservation")
        print("menu")
        print("help")
        print("exit")
        print()

    @staticmethod
    def input_command(database):
        command = ""
        while command != "exit":
            command = input("command>")
            commands = CommandIO.command_parser(command)
            CommandIO.command_choice(database, *commands)

    @staticmethod
    def command_parser(command):
        commands = command.split()

        return (tuple(commands))

    @staticmethod
    def command_choice(database, command, *keywords):
        if command == "show_movies":
            CommandIO.show_movies(database)
        elif command == "show_movie_projections":
            CommandIO.show_movie_projections(database, *keywords)
        elif command == "make_reservation":
            CommandIO.make_reservation(database)
        elif command == "cancel_reservation":
            CommandIO.cancel_reservation(database, *keywords)
        elif command == "menu":
            CommandIO.menu()
        elif command == "help":
            CommandIO.help()
        elif command == "exit":
            CommandIO.exit(database)
        else:
            print("Wrong choice! Please try again!")

    @staticmethod
    def show_movies(database):
        print("Current movies with their rating:")

        movies = database.show_all_movies()

        for movie in movies:
            movie_id = movie[0]
            name = movie[1]
            rating = movie[2]

            print("[{}]  - {} --- {}".format(movie_id, name, rating))

    @staticmethod
    def show_movie_projections(database, movie_id, *date):
        movie_name = database.get_movie_name(movie_id)
        print("Projections for movie: '{}':".format(movie_name))

        projections = database.show_movie_projections(movie_id, *date)

        for projection in projections:
            projection_id = projection[0]
            projection_type = projection[1]
            date = projection[2]
            time = projection[3]

            busy_seats = database.count_non_available_seats(projection_id)
            free_seats = Hall.SEATS - busy_seats

            first_part = "[{}] - {} - {} - ".format(projection_id, date, time)
            second_part = "({}) - ".format(projection_type)
            third_part = "Available Seats: {}".format(free_seats)

            message = first_part + second_part + third_part
            print(message)

    @staticmethod
    def cancel_reservation(database, name):
        database.delete_reservation(name)

    @staticmethod
    def help():
        print()
        print ("1. show_movies")
        print("Show movies ordered by rating descending!")
        print ("2. show_movie_projections <movie_id> [<date>]")
        print("Date is not mandatory! But you must type movie_id!")
        print ("3. make_reservation")
        print("You must follow the steps and everything will be okay!")
        print ("4. cancel_reservation <name>")
        print("Delete your reservation from our system!")
        print ("5. help")
        print("This command will show you this menu!")
        print ("6. exit")
        print("You will exit our system! Be carefull!")
        print()

    @staticmethod
    def exit(database):
        database.close_connection()
        print("\nRservation System closed doors!")
        print("We will see you next time! Goodbye!\n")

    @staticmethod
    def input_name():
        name = input("Please enter your name>")

        return name

    @staticmethod
    def input_tickets():
        tickets = int(input("Please enter number of tickets>"))

        while tickets > Hall.SEATS:
            print("Maximum seats are 100!")
            tickets = int(input("Please enter number of tickets>"))

        return tickets

    @staticmethod
    def input_movie_id():
        movie_id = int(input("Please enter id of movie you want to watch>"))

        return movie_id

    @staticmethod
    def input_projection_id():
        projection_id = int(input("Please enter id of the projection>"))

        return projection_id

    @staticmethod
    def check_seats(database, projection_id, number_of_tickets):

        busy_seats = database.count_non_available_seats(projection_id)
        free_seats = Hall.SEATS - busy_seats

        if free_seats < number_of_tickets:
            return False
        else:
            return True

    @staticmethod
    def append_busy_seats(hall, seats):
        for seat in seats:
            row = seat[0]
            col = seat[1]
            hall.set_busy_seat(row, col)

    @staticmethod
    def choose_seats(busy_seats, number_of_tickets):
        print("Choose row and column for every ticket!")
        all_seats = []
        while number_of_tickets > 0:
            row = None
            col = None

            is_inside_hall = False
            seat_taken = False

            while not is_inside_hall or not seat_taken:
                is_inside_hall = False
                seat_taken = False

                row = int(input("Please choose row>"))
                if row < Hall.MIN_ROW or row > Hall.MAX_ROW:
                    print("Such row didn't exists!")
                    is_inside_hall = False
                    continue

                col = int(input("Please choose col>"))
                if col < Hall.MIN_COL or col > Hall.MAX_COL:
                    print("Such column didn't exists!")
                    is_inside_hall = False
                    continue

                is_inside_hall = True

                if (row, col) in busy_seats:
                    print("The seats are already taken!")
                    seat_taken = False
                    continue

                seat_taken = True

            all_seats.append((row, col))

            number_of_tickets -= 1
            print("Tickets left: {}".format(number_of_tickets))

        return all_seats

    @staticmethod
    def print_movie_name(database, movie_id):
        current_movie = database.get_movie_name(movie_id)[0]
        print("Movie: {}".format(current_movie))

    @staticmethod
    def print_projection_info(database, projection_id, seats):
        current_projection = database.show_projection(projection_id)
        date = current_projection[0]
        time = current_projection[1]
        type = current_projection[2]
        print("Date and Time: {} {} ({})".format(date, time, type))
        print("Seats: {}".format(seats))

    @staticmethod
    def finalize(database, name, projection_id, all_seats):
        finalize = input("type 'finalize'>")
        if finalize == "finalize":
            for seat in all_seats:
                database.add_reservation(name, projection_id, seat[0], seat[1])
        print("Thanks")

    @staticmethod
    def make_reservation(database):
        print("Step 1:")
        name = CommandIO.input_name()
        tickets = CommandIO.input_tickets()

        print("Step 2:")
        CommandIO.show_movies(database)
        movie_id = CommandIO.input_movie_id()

        print("Step 3:")
        is_seats = False

        while not is_seats:
            CommandIO.show_movie_projections(database, movie_id)
            projection_id = CommandIO.input_projection_id()
            is_seats = CommandIO.check_seats(database, projection_id, tickets)

        busy_seats = database.get_non_available_seats(projection_id)

        new_hall = Hall()
        CommandIO.append_busy_seats(new_hall, busy_seats)
        new_hall.print_places()

        print("Step 4: ")
        choosen_seats = CommandIO.choose_seats(busy_seats, tickets)
        CommandIO.append_busy_seats(new_hall, choosen_seats)

        CommandIO.print_movie_name(database, movie_id)
        CommandIO.print_projection_info(database, projection_id, choosen_seats)

        print("Step 5:")
        CommandIO.finalize(database, name, projection_id, choosen_seats)
