class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                index = self.photos[page].index(label) + 1
                return f"{label} photo added successfully on page {page + 1} slot {index}"
        return "No more free spots"

    def display(self):
        result = ""
        dashes = "-----------"
        for page in self.photos:
            photos = ["[]" for _ in range(len(page))]
            result += f"{dashes}\n{' '.join(photos)}\n"
        result += f"{dashes}\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
