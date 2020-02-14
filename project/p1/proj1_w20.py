#########################################
##### Name: Cameron Giniel          #####
##### Uniqname: cginiel             #####
#########################################
import requests
import json
import sys

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
                self.url = json["trackViewUrl"]
            except KeyError:
                self.url = json["collectionViewUrl"]

    def info(self):
        '''
        '''
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        '''
        '''
        return 0

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
            try:
                self.movie_length = json["trackTimeMillis"]
            except KeyError:
                pass

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
    '''we might want to bail on this function and add it to a variable with
    wider scope. you're beginning to give the function too much work to do.
    '''
    search_item = ""
    user_entry = input("Enter a search term, or 'exit' to quit: ")

    if user_entry == "exit":
        sys.exit(0)

    elif user_entry.isalpha():
        user_entry = user_entry

    else:
        if user_entry.isnumeric():
            user_entry = int(user_entry)
    
    search_item = f"term={user_entry}"

    return search_item

def media_list_parser(media_dict_list):
    '''
    '''
    songs = []
    movies = []
    media = []
    counter = 1
    
    # below we loop through all of the dictionaries gathered and add them
    # to their respective media class
    for media_dict in media_dict_list:
        if "kind" in media_dict:
            if media_dict['kind'] == 'song':
                songs.append(Song(json=media_dict))
            elif media_dict['kind'] == 'feature-movie':
                movies.append(Movie(json=media_dict))
                print(f"JSON: {media_dict}")
            else:
                media.append(Media(json=media_dict))
        else:
            media.append(Media(json=media_dict))
   
    # here we present the media cleanly by calling the 
    # class' .info() method that we worked so very hard 
    # to get working under various conditions
    print(f"\nSONGS")
    if len(songs) == 0:
        print(f"None")
    else:
        for song in songs:
            print(f"{counter} {song.info()}")
            counter += 1  

    print(f"\nMOVIES")
    if len(movies) == 0:
        print(f"None")
    else:
        for movie in movies:
            print(f"{counter} {movie.info()}")
            counter += 1

    print(f"\nOTHER MEDIA")
    if len(media) == 0:
        print(f"None\n")
    else:
        for m in media:
            print(f"{counter} {m.info()}")
            counter += 1

    if len(songs) == 0 and len(movies) == 0 and len(media) == 0:
        print("Looks like nothing's here. Check your spelling?\n")


# def more_info():
#     '''
#     '''
#     additional_info = input(f"Enter a number for more info, or a search term, or exit: ")


############################## main #####################################

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    i = 0
    while i >= 0:
        json_to_parse = get_media(params=user_entry_params())
        media_dict_list = json_to_parse['results'] # list of dictionaries
        media_list_parser(media_dict_list)
        # more_info()
        i += 1






