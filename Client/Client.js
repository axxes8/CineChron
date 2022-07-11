console.log("Javascript loaded successfully");

let moviepath = ""
let tvpath = ""

// Opens the navigaiton bar
function openNav() {
    document.getElementById("myTopnav").style.marginLeft = "250px";
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    console.log("Sidebar opened")
  }
  
  // Closes the navigation bar
  function closeNav() {
    document.getElementById("myTopnav").style.marginLeft = "0";
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    console.log("Sidebar Closed")
  }

  async function homepage() {
    document.getElementById("main").innerHTML += "hello world"
    let url = "http://127.0.0.1:8000/get_trending_movies"
    console.log(url)
    let response = await fetch(url)
    let data = await response.json()
    console.log(data)
    
  }

  function moviespage() {
    console.log("moviespage() ran")
    document.getElementById("pagecontent").style.display='none'
    // Pull user input from form, save it in moviepath
    moviepath = document.getElementById("path").value
    localStorage.setItem("moviepathlocal", moviepath)
    console.log("moviepath set to: " + moviepath)
    loadmovies()
  }

  function moviepathtest(){
    console.log("moviepathtest() ran")
    // If moviepath is empty, show form input, else hide it from user
    if (moviepath == ""){
      document.getElementById("pagecontent").style.display='block'
      console.log("element showing")
      console.log("moviepath contains: " + moviepath)
    } else {
      document.getElementById("pagecontent").style.display='none'
      console.log("element hidden")
    }
  }

  async function loadmovies(){
    console.log("loadmovies() ran")
    // Hide form input box from user
    document.getElementById("movie_details").style.display='none'
    document.getElementById("pagecontent").style.display='none'
    console.log("element hidden")
    // Show movies to user
    document.getElementById("grid").style.display=''
    // Set url to function in FastAPI
    let url = "http://127.0.0.1:8000/sys_info/" + moviepath
    console.log(url)
    // Get request to url
    let response = await fetch(url)
    let data = await response.json()
    console.log(data)
    // Parse data and show it on the page
    data.forEach(element => {
      document.getElementById("grid").innerHTML += "<div onclick='moviedetails(" + element.movie_id + ")'> <div><h3>" + element.title + "</h3></div> <div><img src='" + element.poster_path + "' width=250> </div></div>"
      console.log(element.movie_id)
    });
  }
  
  // Hide the movie details and show the movie grid
  function showgrid(){
    document.getElementById("grid").style.display=''
    document.getElementById("movie_details").style.display='none'
  }

  async function moviedetails(id){
    console.log("moviedetails() ran")
    // Hide movie screen from user
    document.getElementById("grid").style.display='none'
    document.getElementById("movie_details").style.display=''
    let url = "http://127.0.0.1:8000/get_movie_details/" + id
    console.log(url)

    let response = await fetch(url)
    let data = await response.json()
    console.log(data)
    document.getElementById("movie_details").innerHTML = "<button class='backbtn' onclick='showgrid()'>Back to movie list</button><br><div class='container'><div><img src='https://image.tmdb.org/t/p/original"+ data.poster_path +"'height=700></div><div><h1>"+ data.title +"</h1><p>Overview: "+ data.overview +"</p><p>Release Date: "+ data.release_date +"</p><p>Runtime: "+ data.runtime +" Minutes</p></div></div>"
  }

  function tvshowspage() {
    console.log("tvshowpage() ran")
    tvpath = document.getElementById("path").value
    console.log("tvpath set to: " + tvpath)
    loadtvshows()
  }

  function tvpathtest(){
    console.log("tvpathtest() ran")
    if (tvpath == ""){
      document.getElementById("pagecontent").style.display='block'
      console.log("element showing")
      
    } else {
      document.getElementById("pagecontent").style.display='none'
      console.log("element hidden")
    }
  }

  function loadtvshows(){
    console.log("loadtvshows() ran")
    document.getElementById("pagecontent").style.display='none'
    console.log("element hidden")
  }