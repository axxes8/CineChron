import os
import glob
import json
import os
import threading
# from urllib import response

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

#Global variables for the server to try to cache objects
Server_path = ""
Server_info = ""

#This class is for cacheing the movies in a dictionary and also storing the path as well
#Takes in the path. Retrieves the files from the get filename function, and gets all the movies from TMDB
class System_info:

    def __init__(self, path):
        super().__init__()
        self.server_path = path
        print(path)
        self.path_list = json.loads(get_filename(path))
        self.movie_dict = dict()
        #self.genre_key = get_genre_list()

        get_movies(self.path_list,self.movie_dict)
        
    #function that is used for if the path needs to be changed from when the object was created
    def update_movies(self,path):
        self.server_path = path
        self.path_list = json.loads(get_filename(path))
        self.movie_dict = dict()

        get_movies(self.path_list,self.movie_dict)

    #return all the movie jsons for the home page with only the details that are needed
    def home_page(self):
        final_json = []
        for movie in self.movie_dict.values():
            final_json.append(json.loads(movie.get_home_json()))
        return json.dumps(final_json)

    #take in a movie ID from the client, search the cached movie dictionary. Return the full json for the client.
    def get_movie_details(self,id):
        movie = self.movie_dict[id]
        return movie.get_full_details()



#This class is used to extract all the json data from the Movie DB API.  
class Movie:
    
    #pull out all the items from the json that you would like from the source json to be stored in the python object.
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

    #take the details from the object and dump them as a json string that can be "loaded" by Fast Api to the client 
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
            }
        return json.dumps(output_json)

    #json details that are only dumped for the home page
    def get_home_json(self):
        home_json = {
              "movie_id": self.movie_id,
              "title": self.title,
              "poster_path": self.poster_path
            }
        return json.dumps(home_json)

    #make a Api call to the TMDB for the full details json of that specific movie
    def get_full_details(self):

        Movie_details = f"https://api.themoviedb.org/3/movie/{self.movie_id}?api_key={api_key}&language=en-US"
        details = API_request(Movie_details)

        details.start()
        details.join()

        return details.response

    #make a api call for the trending movies that are stored in TMDB.
    def get_trending(self):
        trend_m_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
        call_m = API_request(trend_m_url)

        call_m.start()
        call_m.join()

        return call_m.response

    #create a thread for the json of movies that are similar to the current movie object.
    def get_similar_movies(self):
        similar_movies_url = f"https://api.themoviedb.org/3/movie/{self.movie_id}/similar?api_key={api_key}&language=en-US&page=1"
        similar = API_request(similar_movies_url)

        similar.start()
        similar.join()

        return similar.response


#empty class for TV shows
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

#Create a Thread that calls the desired URL, 
#Since this one is searched requests it will have a list of results but the response will be the first result of the list.
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

#Single thread request for the desired URL that is provided
#If the status code it successful (200) then the returned json will be stored in the object.response
#if the status code is anything other than 200 a error message will be printed.
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

# funtion takes in a list of movies from get_filename and then a empty (or filled) dictionary.
# A list API request will be created for each of the movies---->started---->then joined)
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
        # if the response is not empty then create a movie object and add it to the dictionary.
        if len(thread[0].response) == 0:
            #not_found.append(movie) 
            print(f"The movie file {thread[1]} couldnt be found. Make sure the filename is labled as simply the movie title")
        else:
            movie = Movie(thread[0].response,thread[1],thread[2])
            library_dict[thread[0].response["id"]] = movie

#function to make a API TMDB call for the full details of the movie ID that is passed into the function.
def get_movie_full_details(id):
    Movie_details = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&language=en-US"
    details = API_request(Movie_details)
    details.start()
    details.join()
    return details.response

def get_tv_show_full_details():
    #url = TV_search + name
    pass

def get_similar_movies(movie_id):
    similar_movies_url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={api_key}&language=en-US&page=1"
    similar = API_request(similar_movies_url)

    similar.start()
    similar.join()

    return similar.response


#Function creates a thread that retrives all trending movies, tv shows, and people from TMBD 
def get_trending_all_media():
    trend_all_url = f"https://api.themoviedb.org/3/trending/all/day?api_key={api_key}"
    call_all = API_request(trend_all_url)

    call_all.start()

    call_all.join()

    return call_all.response["results"]

#Function that creates a thread that retrieves the Jsons of the trending Movies
def get_trending_movies():
    trend_m_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
    call_m = API_request(trend_m_url)

    call_m.start()

    call_m.join()

    return call_m.response["results"]

#Function that creates a thread that retrieves the Jsons of the trending TV shows
def get_trending_tv_shows():
    trend_t_url = f"https://api.themoviedb.org/3/trending/tv/day?api_key={api_key}"
    call_tv = API_request(trend_t_url)

    call_tv.start()

    call_tv.join() 

    return call_tv.response["results"]

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
    path = path + "/**/*.m*"
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
    
    trend_movies = get_trending_movies()

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
