console.log("Javascript loaded successfully")

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
    document.getElementById("main").innerHTML = "Cinechron";
  }

  function moviespage() {
    document.getElementById("main").innerHTML = "Movies";
  }

  function tvshowspage() {
    document.getElementById("main").innerHTML = "TV Shows";
  }