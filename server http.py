import http.server
import socketserver
import os
import json
import threading
import requests

#PORT = 8000
#
#web_dir = os.path.join(os.path.dirname(__file__), 'D:/Users/Taylor/Desktop')
#os.chdir(web_dir)
#
#Handler = http.server.SimpleHTTPRequestHandler
#httpd = socketserver.TCPServer(("", PORT), Handler)
#print("serving at port", PORT)
#httpd.serve_forever()

api_key = '9ba37aca04338a3886c632201a0a7dce'
Movie_search = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query="
Genre = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
Test_movie = "F9"

class Movie:
    
    def __init__(self, json):
        super().__init__()
        self.genres = json["genre_ids"]
        self.movie_id = json["id"]
        self.title = json["original_title"]
        self.overview = json["overview"]
        self.popularity = json["popularity"]
        self.poster = json["poster_path"]
        self.release_date = json["release_date"]


    def add_title(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass

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

class TV_Show:
    
    def __init__(self, json):
        super().__init__()

    def add_title(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass


class Searched_API_request(threading.Thread):
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
            self.response = self.listed_results[0]
        else:
            print("Error retrieveing data on ",self.url)

def get_movie(name,movie_file):
    url = Movie_search + name
    json = API_request(url)
    json.start()
    json.join()
    movie = Movie(json.response)
    return movie

def get_tv_show(name,tv_file):
    url = Movie_search + name
    pass

def get_genre_list():



def main():
    movie_data = get_movie(Test_movie,Test_movie)

    print(movie_data.title)
    print(movie_data.overview)


if __name__ == "__main__":
    main()