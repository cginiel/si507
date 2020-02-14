#########################################
##### Name: Cameron Giniel          #####
##### Uniqname: cginiel             #####
#########################################
import requests
import json

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
            try:
                self.title = json["trackName"]
            except KeyError:
                self.title = json["collectionName"]

            try:
                self.author = json["artistName"]
            except KeyError:
                self.title = json["collectionName"]

            try:
                self.release_year = json["releaseDate"][0:4]
            except KeyError:
                pass

            try:
                self.url = json["collectionViewUrl"]
            except KeyError:
                self.url = json["trackViewUrl"]

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

def user_entry_params():
    '''
    '''
    user_entry = input("Enter a search term, or 'exit' to quit: ")

    search_item = f"term={user_entry}"

    return search_item

def media_list_parser(media_dict_list):
    '''
    '''
    songs = []
    movies = []
    media = []
     
    for media_dict in media_dict_list:
        if "kind" in media_dict:
            if media_dict['kind'] == 'song':
                print(f"SONG: {media_dict}\n")
                songs.append(Song(json=media_dict))
            elif media_dict['kind'] == 'feature-movie':
                print(f"MOVIE: {media_dict}\n")
                movies.append(Movie(json=media_dict))
            else:
                print(f"OTHER MEDIA: {media_dict}\n")
                media.append(Media(json=media_dict))
        else:
            media.append(Media(json=media_dict))

    print("\nSONGS")
    counter = 1
    for song in songs:
        print(f"{counter} {song.info()}")
        counter += 1  
    print("\nMOVIES")
    for movie in movies:
        print(f"{counter} {movie.info()}")
        counter += 1
    print("\nMEDIA")
    for m in media:
        print(f"{counter} {m.info()}")
        counter += 1

############################## main #####################################

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    json_to_parse = get_media(params=user_entry_params())
    media_dict_list = json_to_parse['results'] # list of dictionaries
    media_list_parser(media_dict_list)






