class Score():
    def __init__(self, movie, plot, actors, music):
        self.movieName = movie
        self.plot_rating = plot
        self.actor_rating = actors
        self.music_rating = music

        self.averageRating = int((self.plot_rating + self.actor_rating + self.music_rating)/3)

        self.archive = {
            "Movie Name": self.movieName, "Plot": self.plot_rating, "Acting": self.actor_rating, "Music": self.music_rating , "Avg Rating" : self.averageRating
        }

    def showData(self):
        print(self.averageRating)
        print(self.archive)

m = Score("Se7en", 4, 3 ,5)
m.showData()








