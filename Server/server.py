import os
import glob
import json
import os
import threading
from urllib import response

import requests
# import vlc

#Movie DB API referance = https://developers.themoviedb.org/3/getting-started/introduction

#Movie DB API key https://api.themoviedb.org
api_key = '9ba37aca04338a3886c632201a0a7dce'

#API call that returns a result set of movies 
Movie_search = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query="

#API call that returns the genre list 
Genre = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"

#test movie variable
Test_movie = "Over the Hedge"

#This class is for cacheing the movies in a dictionary and also storing the path as well
class System_info:

    def __init__(self, path):
        super().__init__()
        self.server_path = path
        print(path)
        self.path_list = json.loads(get_filename(path))
        self.movie_dict = dict()
        #self.genre_key = get_genre_list()

        get_movies(self.path_list,self.movie_dict)
        

    def update_movies(self):
        path = self.server_path
        movies = self.path_list

    def home_page(self):
        final_json = []
        for movie in self.movie_dict.values():
            final_json.append(json.loads(movie.get_home_json()))
        return json.dumps(final_json)

    def get_movie_details(self):
        pass





#This class is used to extract all the json data from the Movie DB API.  
class Movie:
    
    def __init__(self, TMDB_json, file_title, file_path):
        super().__init__()
        
        self.file_title = file_title
        self.file_path = file_path
        self.movie_id = TMDB_json["id"]
        self.title = TMDB_json["original_title"]
        self.overview = TMDB_json["overview"]
        self.popularity = TMDB_json["popularity"]
        self.poster_path = "https://image.tmdb.org/t/p/original" + TMDB_json["poster_path"]
        self.release_date = TMDB_json["release_date"]
        self.genre_ids = TMDB_json["genres"]


    def get_json(self):
        output_json = {
              "file_title": self.file_title,
              "file_path": self.file_path,
              "movie_id": self.movie_id,
              "title": self.title,
              "overview": self.overview,
              "popularity": self.popularity,
              "poster_path": self.poster_path,
              "release_date": self.release_date,
              "genres": self.genres
            }
        return json.dumps(output_json)

    def get_home_json(self):
        home_json = {
              "file_title": self.file_title,
              "file_path": self.file_path,
              "poster_path": self.poster_path
            }
        return json.dumps(home_json)

    def get_full_details(self):

        Movie_details = f"https://api.themoviedb.org/3/movie/{self.movie_id}?api_key={api_key}&language=en-US"
        details = API_request(Movie_details)

        details.start()
        details.join()

        return details.response


    def get_trending(self):
        trend_m_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
        call_m = API_request(trend_m_url)

        call_m.start()
        call_m.join()

        return call_m.response


    def get_similar_movies(self):
        similar_movies_url = f"https://api.themoviedb.org/3/movie/{self.movie_id}/similar?api_key={api_key}&language=en-US&page=1"
        similar = API_request(similar_movies_url)

        similar.start()
        similar.join()

        return similar.response

    def __str__(self):
        pass


#empty class for 
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

def get_movies(movie_list, library_dict):
    threads = []
    for movie in movie_list:
        url = Movie_search + movie["Title"]
        Title = movie["Title"]
        path = movie["path"]
        json = Searched_request(url)
        threads.append((json,Title,path))
    
    for thread in threads:
        thread[0].start()

    for thread in threads:
        thread[0].join()
        if len(thread[0].response) == 0:
            #not_found.append(movie) 
            print(f"The movie file {thread[1]} couldnt be found. Make sure the filename is labled as simply the movie title")
        else:
            movie = Movie(thread[0].response,thread[1],thread[2])
            library_dict[thread[0].response["id"]] = movie

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
    ## Path is as follows: Driveletter:/directories/**/<filename>.<Filetype>
    ##      The ** denotes iterating through the directory
    ##      * can be used as a wildcard
    # path="Z:/**/*.*"
    ## Add iterator and wildcards to path
    path = path + "/**/*.*"
    ## Strip quotations off of path
    stripped_path = path.strip('"')
    # print(stripped_path)
    json_movieList = []
    
    ## Recursivly searches through path finding all files and returns the path for each file.
    for file in glob.iglob(stripped_path, recursive=True):
        ## Strip off the path and file extention, brackets and single quotations, then append the file name to 'json_movieList'
        ## Add absolute path to 'json_movieList
        filename = str(os.path.basename(file).split('.')[:-1]).strip('[]').strip('\'')
        filepath = str(os.path.abspath(file))

        json_movieList.append({'Title': filename, 'path': filepath})
    ## Convert list to JSON
    json_dump = json.dumps(json_movieList)

    ## Print json_dump and number of movies found to the console.
    print(json_dump)
    print("Found", len(json_movieList), "files.")

    return(json_dump)

def main():
    #movie_list = get_filename()
    genre_list = get_genre_list()
    library_dict = dict()
    movie = get_movies(Test_movie,library_dict,genre_list)
    
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
