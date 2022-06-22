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
    let path = ""
    let url = "localhost:8000/sys_info/" + path
    if (path == ""){
      document.getElementById("pathinput").style.display = "block"
    }

    else{
      document.getElementById("pathinput").style.display = "none"
      // let response = await fetch(url);
      // let data = await response.json();
      // return data;
    }
    // document.getElementById("main").innerHTML = "Movies";
  }

  function tvshowspage() {
    document.getElementById("main").innerHTML = "TV Shows";
  }