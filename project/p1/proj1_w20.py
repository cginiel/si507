#########################################
##### Name: Cameron Giniel          #####
##### Uniqname: cginiel             #####
#########################################
import requests


class Media:
    '''ADD DOCSTRING
    '''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json=None):
        '''
        '''
        if (json is None):
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            self.title = json["collectionName"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][0:4]
            self.url = json["collectionViewUrl"]

    def info(self):
        '''
        '''
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        '''
        '''
        return 0


# Other classes, functions, etc. should go here
class Song(Media): # specific to this class: album, genre, tracklength
    '''ADD DOCSTRING
    '''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0, json=None):
        # do these inits need defaults if they're inherited from superclass?
        '''ADD DOCSTRING
        '''
        super().__init__(title, author, release_year, url)
        self.album = album
        self.genre = genre
        self.track_length = track_length

    def info(self):
        '''ADD DOCSTRING
        '''
        return f"{super().info()} [{self.genre}]" 

    def length(self):
        '''ADD DOCSTRING
        '''
        rounded_length = round(self.track_length/1000)
        return rounded_length # figure out API's track length and do arithmetic to solve

class Movie(Media): # specific to this class: rating, movielength
    '''ADD DOCSTRING
    '''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0, json=None):
        '''ADD DOCSTRING
        '''
        super().__init__(title, author, release_year, url) # do I need URL here?
        self.rating = rating
        self.movie_length = movie_length

    def info(self):
        '''ADD DOCSTRING
        '''
        return f"{super().info()} [{self.rating}]"

    def length(self):
        '''ADD DOCSTRING
        '''
        rounded_length = round((self.movie_length/1000)/60)
        return rounded_length



if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
