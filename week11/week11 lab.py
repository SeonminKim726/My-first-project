'''
#10-a
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
    def display_info(self):
        print(f"{self.title} {self.author}")
    def __str__(self):
        print(f"{self.title} by {self.author}")


#10-b
class Library:
    def __init__()

'''


#12-
class TVshow:
    def __init__(self, title = "Unknown", genre = "Unknown"):
        self.title = title
        self.genre = genre
    
    def get_genre(self):
        return self.genre
    def get_title(self):
        return self.title
    
    def set_genre(self, _genre):
        self.genre = _genre
    def set_title(self, _title):
        self.title = _title

    def __str__(self):
        return f"The movie is: {self.get_title()} and the gnere is: {self.get_genre()}"
    

class NetflixDashboard:
    def __init__(self, profile_name = "Unknown"):
        self.TVshows = []
        self.profile_name = profile_name

    def add_show(self, show):
        self.TVshows.append(show)

    def display_recommendatoins(self):
        for show in self.TVshows:
            print(show)

tvshow1 = TVshow("Two and a half men", "sitcom")
tvshow2 = TVshow("Friends", "sitcom")

profile1 = NetflixDashboard("Evan")
profile1.add_show(tvshow1)
profile1.add_show(tvshow2)

profile1.display_recommendatoins()


