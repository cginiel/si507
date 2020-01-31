#########################################
##### Name: Cameron Giniel          #####
##### Uniqname: cginiel             #####
#########################################

class Media:
	'''ADD DOCSTRING
	'''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL"):
    	'''
    	'''
        self.title = title
        self.author = author
        self.release_year = release_year
        self.url = url ## ask about this in OH

    def info(self):
    	'''
    	'''
    	print(self.title + " by " + self.author + f" ({self.release_year})")

    def length():
    	'''
    	'''
    	return 0


# Other classes, functions, etc. should go here
class Song(Media):
	'''ADD DOCSTRING
	'''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0):
    	# do these inits need defaults if they're inherited from superclass?
    	'''ADD DOCSTRING
    	'''
    	super().__init__(title, author, release_year) # do i need URL here?
    	self.album = album
    	self.genre = genre
    	self.track_length = track_length

    def info(self, genre):
    	'''ADD DOCSTRING
    	'''
    	return super().info() + f" [{genre}]" # do I need self.genre?

    def length(self, track_length):
    	'''ADD DOCSTRING
    	'''
    	rounded_length = round(track_length/1000)
    	return print(rounded_length) # figure out API's track length and do arithmetic to solve

class Movie(Media):
	'''ADD DOCSTRING
	'''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0):
    	'''ADD DOCSTRING
    	'''
    	super().__init__(title, author, release_year) # do I need URL here?
    	self.rating = rating
    	self.movie_length = movie_length

    def info(self, rating):
    	'''ADD DOCSTRING
    	'''
    	return super().info() + f" [{rating}]" # do I need self.rating?

    def length(self, movie_length):
    	'''ADD DOCSTRING
    	'''
    	rounded_length = round((movie_length/1000)/60)
    	return print(rounded_length)



if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
