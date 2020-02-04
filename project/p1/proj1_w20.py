#########################################
##### Name: Cameron Giniel          #####
##### Uniqname: cginiel             #####
#########################################
import requests

######## construct classes #############
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
        super().__init__(title, author, release_year, url, json)
        if (json is None):
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            self.title = json["trackName"]
            self.album = json["collectionName"]
            self.genre = json["primaryGenreName"]
            self.track_length = json["trackTimeMillis"]

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
        super().__init__(title, author, release_year, url, json)
        if (json is None):
            self.rating = rating
            self.movie_length = movie_length
        else:
            self.title = json["trackName"]
            self.rating = json["contentAdvisoryRating"]
            self.movie_length = json["trackTimeMillis"]

    def info(self):
        '''ADD DOCSTRING
        '''
        return f"{super().info()} [{self.rating}]"

    def length(self):
        '''ADD DOCSTRING
        '''
        rounded_length = round((self.movie_length/1000)/60)
        return rounded_length



######## fetching media data from iTunes API ##########
BASE_URL = "https://itunes.apple.com/search" # only interested in media

def get_media(url=BASE_URL, params=None):
    '''
    '''
    if params:
        response = requests.get(url, params=params).json()
    else:
        response = requests.get(url, params=params).json()

    return response

##### im trying to write a function for user entry that can be applied ####
##### to search the API using the get_media() function ####################
def user_entry(input):
    media_type = ""
    media_type = input("Enter a search term, or \"exit\" to quit: ")

user_entry = None

while user_entry == None:
    media_type = input("Enter a search term, or \"exit\" to quit: ")
    if media_type.isalpha():
        media_type = str(media_type)
    
    #### MEDIA ####







if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
