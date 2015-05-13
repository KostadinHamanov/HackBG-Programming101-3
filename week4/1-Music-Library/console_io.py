class ConsoleIO:

    @staticmethod
    def print_menu():
        print ("-" * 50)
        print ("MUSIC PLAYER")
        print ("Please enter the command in the brackets")
        print ("-" * 50)
        print ("(generate) Generate playlist from directory")
        print ("(show) Show playlist")
        print ("(next) Play next song")
        print ("(shuffle) Change shuffle")
        print ("(repeat) Change repeat")
        print ("(stop) Stop song")
        print ("(menu) Menu")
        print ("(exit) Exit")
        print ("-" * 50)

    @staticmethod
    def get_command(player):

        while True:
            input_command = input("command>")

            command = input_command.lower()

            if command == "generate":
                directory = input("directory>")
                player.add_songs_from_directory(directory)
                print("Songs added to playlist!")

            elif command == "show":
                print (player.show_playlist())

            elif command == "next":
                player.stop()
                name = player.play_next_song()
                print ("Playing: {}". format(name))

            elif command == "shuffle":
                value = input("Enter shuffle mode (True or False)>")
                player.change_shuffle_mode(bool(value))
                print("Shuffle mode changed")

            elif command == "repeat":
                value = input("Enter repeat mode (True or False)>")
                player.change_repeat_mode(bool(value))

            elif command == "stop":
                player.stop()
                print ("Song stopped")

            elif command == "menu":
                ConsoleIO.print_menu()

            elif command == "exit":
                player.stop()
                break

            else:
                print("Please enter valid command")
