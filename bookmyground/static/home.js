// $(document).ready(function() {
//     $(".menu-icon").on("click", function() {
//           $("nav ul").toggleClass("showing");
//     });
// });

// // Scrolling Effect

// $(window).on("scroll", function() {
//     if($(window).scrollTop()) {
//           $('nav').addClass('black');
//     }

//     else {
//           $('nav').removeClass('black');
//     }
// })

$(document).ready(function() {
    // Transition effect for navbar 
    $(window).scroll(function() {
      // checks if window is scrolled more than 500px, adds/removes solid class
      if($(this).scrollTop() > 425) { 
          $('nav').addClass('black');
      } else {
          $('nav').removeClass('black');
      }
    });
});

// location fetch 
const blocation = document.querySelector('.blocation');


blocation.addEventListener("click", ()=>{
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(onSuccess, onError);
    }else{
        blocation.innerText = "Your browser not support";
    }
});

function onSuccess(position){
    
    let {latitude, longitude} = position.coords;
    fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=cbacce3ec2ea4b2891c1ec29a9393a43`)
    .then(response => response.json()).then(response =>{
        let allDetails = response.results[0].components;
        console.table(allDetails);
        let {city,state} = allDetails;
        blocation.innerText = `${city} `;
    }).catch(()=>{
        blocation.innerText = "Something went wrong";
        document.getElementById("citychoice").href = "/booking?city=none&area=none&sport=none";
    });
}

function onError(position){

    if(error.code == 2){
        button.innerText = "Location is unavailable";
    }else{
        button.innerText = "Something went wrong";
    }
    button.setAttribute("disabled", "true");
}



  





