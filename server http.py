import http.server
import socketserver
import os
import json
import threading
import requests

PORT = 8000

web_dir = os.path.join(os.path.dirname(__file__), 'D:/Users/Taylor/Desktop')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

api_key = '9ba37aca04338a3886c632201a0a7dce'
Base_URL = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query="
Test_movie = "Jack reacher"

class Movie:
    
    def __init__(self, json):
        super().__init__()

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


class Movie_Series:
    
    def __init__(self, json):
        super().__init__()

    def add_movie(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass

class TV_Series:
    
    def __init__(self, json):
        super().__init__()

    def add_episode(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass


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

def get_movie(name):
    url = Base_URL + name
    json = API_request(url)
    json.start()
    json.join()

    return json.response


def main():
    movie_data = get_movie(Test_movie)

    print(movie_data)


if __name__ == "__main__":
    main()