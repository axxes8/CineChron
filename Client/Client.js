console.log("Javascript loaded successfully");

let moviepath = ""
let tvpath = ""

function openNav() {
    document.getElementById("myTopnav").style.marginLeft = "250px";
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    console.log("Sidebar opened")
  }
  
  function closeNav() {
    document.getElementById("myTopnav").style.marginLeft = "0";
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    console.log("Sidebar Closed")
  }

  function homepage() {
  
  }

  function moviespage() {
    console.log("moviespage() ran")
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
    document.getElementById("pagecontent").style.display='none'
    console.log("element hidden")
    // Set url to function in FastAPI
    let url = "http://127.0.0.1:8000/sys_info/" + moviepath
    console.log(url)
    // Get request to url
    let response = await fetch(url)
    let data = await response.json()
    console.log(data)
    // Parse data and show it on the page
    data.forEach(element => {
      document.getElementById("grid").innerHTML += "<div> <div><h3>" + element.title + "</h3></div> <div><img src='" + element.poster_path + "' width=250> </div></div>"
    });
    
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