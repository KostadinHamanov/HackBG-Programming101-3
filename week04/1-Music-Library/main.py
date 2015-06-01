from console_io import ConsoleIO
from music_player import MusicPlayer


def main():

    my_playlist = MusicPlayer("NewPlaylist")
    ConsoleIO.print_menu()
    ConsoleIO.get_command(my_playlist)

if __name__ == '__main__':
    main()
