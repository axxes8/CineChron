import os
import glob
import json
import os
import threading

import requests
# import vlc

#Movie DB API key https://api.themoviedb.org
api_key = '9ba37aca04338a3886c632201a0a7dce'

#API call that returns a result set of movies 
Movie_search = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query="

#API call that returns the genre list 
Genre = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"

Test_movie = "Over the Hedge"

#This class is used to extract all the json data from the Movie DB API.  
class Movie:
    
    def __init__(self, TMDB_json, genre_json):
        super().__init__()
        
        self.movie_id = TMDB_json["id"]
        self.title = TMDB_json["original_title"]
        self.overview = TMDB_json["overview"]
        self.popularity = TMDB_json["popularity"]
        self.poster_path = TMDB_json["poster_path"]
        self.release_date = TMDB_json["release_date"]

        self.genre_ids = TMDB_json["genre_ids"]
        self.genre_key = genre_json["genres"]

        self.genres = []

        for genre in self.genre_ids:
            for key in self.genre_key:
                if genre == key["id"]:
                    self.genres.append(key["name"]) 

    def get_json(self):
        output_json = {
              "movie_id": self.movie_id,
              "title": self.title,
              "overview": self.overview,
              "popularity": self.popularity,
              "poster_path": self.poster_path,
              "release_date": self.release_date,
              "genres": self.genres,
            }
        return json.dumps(output_json)

    def get_trending():
        trend_m_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
        call_m = API_request(trend_m_url)

        call_m.start()

        call_m.join()

        return call_m.response

    def __str__(self):
        pass


#
class TV_episode:
    
    def __init__(self, json):
        super().__init__()

    def add_season(self, id):
        pass

    def add_edisode(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass

#
class TV_Show:
    
    def __init__(self, json):
        super().__init__()

    def add_title(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass

#
class Searched_request(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}
        self.listed_results = []

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            movies_returned = response.json()
            self.listed_results = movies_returned["results"]
            if len(self.listed_results) < 1:
                print("No results found")
            else:
                self.response = self.listed_results[0]
        else:
            print("Error retrieveing data on ",self.url)

#
class API_request(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.response = response.json()
        else:
            print("Error retrieveing data on ",self.url)

def get_movie(name, library_dict, genre_dict):
    url = Movie_search + name
    json = Searched_request(url)
    json.start()
    json.join()
    if len(json.response) == 0:
        movie = f"The movie file {name} couldnt be found. Make sure the filename is labled as simply the movie title"
    else:
        movie = Movie(json.response,genre_dict)
        library_dict[name] = movie
    return movie

def get_tv_show(name,tv_file):
    #url = TV_search + name
    pass

#Function creates two threads to the Movie DB API. One thread retrieves a list of  
def get_trending():
    trend_m_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
    call_m = API_request(trend_m_url)

    trend_t_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
    call_tv = API_request(trend_t_url)

    call_m.start()
    call_tv.start()

    call_m.join()
    call_tv.join() 

    return call_m.response, call_tv.response

#Function creates a thread that gets the list of genres with their genre ID connected.
def get_genre_list():
    genres_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    genre_list = API_request(genres_url)
    genre_list.start()
    genre_list.join()

    return genre_list.response

def get_filename(path):
    ## Pathname is as follows: Driveletter:/directories/**/<filename>.<Filetype>
    ##      The ** denotes iterating through the directory
    ##      * can be used as a wildcard
    # path="Z:/**/*.*"

    stripped_path = path.strip('"')
    # print(stripped_path)
    movieList = []
    
    ## Recursivly searches through path finding all files and returns the path for each file.
    for file in glob.iglob(stripped_path, recursive=True):
        ## Strip off the path and append the file name to 'movieList'
        movieList.append(os.path.basename(file))
        # print(os.path.basename(file))
        
    print(movieList)
    print("Found", len(movieList), "files.")

    return(movieList)

def main():
    #movie_list = get_filename()
    genre_list = get_genre_list()
    library_dict = dict()
    movie = get_movie(Test_movie,library_dict,genre_list)
    
    trend_movies,trend_tv = get_trending()

    print(movie.title)
    print(movie.overview)
    print(movie.genres)
    test = movie.get_json()

    #t = json.loads(test)
    #print(json.dumps(t))


    #print(genre_list)
    #print(trend_movies)
    #print(trend_tv)


if __name__ == "__main__":
    main()
