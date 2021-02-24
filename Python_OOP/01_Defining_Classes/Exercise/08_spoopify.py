class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = float(length)
        self.single = bool(single)

    def get_info(self):
        return f"{self.name} - {self.length}"


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if self.published:
            return f"Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."
        song_finder = [s for s in self.songs if s.name == song_name]
        if not song_finder:
            return f"Song is not in the album."
        self.songs.remove(song_finder[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = f"Album {self.name}\n"
        for s in self.songs:
            info += f"== {s.get_info()}\n"
        return info


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        album_finder = [a for a in self.albums if a.name == album_name]
        if not album_finder:
            return f"Album {album_name} is not found."
        elif album_finder[0].published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(album_finder[0])
        return f"Album {album_name} has been removed."

    def details(self):
        data = f"Band {self.name}\n"
        for a in self.albums:
            data += f"{a.details()}\n"
        return data

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())