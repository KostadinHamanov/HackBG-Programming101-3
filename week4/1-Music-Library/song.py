class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        length_info = [x.strip() for x in length.split(':')]
        if len(length_info) == 3:
            self.hours = int(length_info[0])
            self.minutes = int(length_info[1])
            self.seconds = int(length_info[2])
            self.length = length
        elif len(length_info) == 2:
            self.minutes = int(length_info[0])
            self.seconds = int(length_info[1])
            self.length = length
        else:
            raise ValueError("Length not proper format: {}". format(length))

    def __str__(self):
        return "{} - {} from {} - {}" \
            .format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        # titles = self.title == other.title
        # artists = self.artist == other.artist
        # albums = self.album == other.album
        # lenghts = self.length == other.length
        # return titles and artists and albums and lenghts
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.__str__())

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.hours * 60 + self.minutes

    def get_seconds(self):
        return self.get_minutes() * 60 + self.seconds

    def get_length(self, seconds=False, minutes=False, hours=False):
        if not seconds and not minutes and not hours:
            return str(self.length)

        if seconds:
            return self.get_seconds()

        if minutes:
            return self.get_minutes()

        if hours:
            return self.get_hours()

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key]
                for key in song_dict if not key.startswith("_")}

