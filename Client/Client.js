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
    moviepath = document.getElementById("path").value
    localStorage.setItem("moviepathlocal", moviepath)
    console.log("moviepath set to: " + moviepath)
    loadmovies()
  }

  function tvshowspage() {
    console.log("tvshowpage() ran")
    tvpath = document.getElementById("path").value
    console.log("tvpath set to: " + tvpath)
    loadtvshows()
  }

  function moviepathtest(){
    // console.log("moviepathtest() ran")
    if (moviepath == ""){
      document.getElementById("pathinput").style.display='block'
      console.log("element showing")
      console.log("moviepath contains: " + moviepath)
    } else {
      document.getElementById("pathinput").style.display='none'
      console.log("element hidden")
      // moviespage()
    }
  }

  function tvpathtest(){
    // console.log("tvpathtest() ran")
    if (tvpath == ""){
      document.getElementById("pathinput").style.display='block'
      console.log("element showing")
      
    } else {
      document.getElementById("pathinput").style.display='none'
      console.log("element hidden")
      // tvshowspage()
    }
  }

  function loadmovies(){
    console.log("loadmovies() ran")
    document.getElementById("pathinput").style.display='none'
    console.log("element hidden")
  }

  function loadtvshows(){
    console.log("loadtvshows() ran")
    document.getElementById("pathinput").style.display='none'
    console.log("element hidden")
  }