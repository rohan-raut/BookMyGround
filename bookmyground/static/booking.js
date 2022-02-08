
function set_city() {
    url = "http://127.0.0.1:8000/api/cities";
    fetch(url)
        .then(response => response.text())
        .then(data => {
            let json = JSON.parse(data);
            let list = "<option value='none'>--Select--</option>\n";
            for (let i = 0; i < json.length; i++) {
                list = list + "<option value='" + json[i]['city'] + "'>" + json[i]['city'] + "</option>\n";
            }
            document.getElementById("select_city").innerHTML = list;
        });
}

function set_area() {
    if (document.getElementById("select_city").value != "none") {
        url = "http://127.0.0.1:8000/api/areas?city=" + document.getElementById("select_city").value;
        fetch(url)
            .then(response => response.text())
            .then(data => {
                let json = JSON.parse(data);
                let list = "<option value='none'>--Select--</option>\n";
                for (let i = 0; i < json.length; i++) {
                    list = list + "<option value='" + json[i]['area'] + "'>" + json[i]['area'] + "</option>\n";
                }
                document.getElementById("select_area").innerHTML = list;
            });
    }
    else {
        url = "http://127.0.0.1:8000/api/areas";
        fetch(url)
            .then(response => response.text())
            .then(data => {
                let json = JSON.parse(data);
                let list = "<option value='none'>--Select--</option>\n";
                for (let i = 0; i < json.length; i++) {
                    list = list + "<option value='" + json[i]['area'] + "'>" + json[i]['area'] + "</option>\n";
                }
                document.getElementById("select_area").innerHTML = list;
            });
    }
}

function set_sport() {
    url = "http://127.0.0.1:8000/api/sports";
    fetch(url)
        .then(response => response.text())
        .then(data => {
            let json = JSON.parse(data);
            let list = "<option value='none'>--Select--</option>\n";
            for (let i = 0; i < json.length; i++) {
                list = list + "<option value='" + json[i]['sport_ground'] + "'>" + json[i]['sport_ground'] + "</option>\n";
            }
            document.getElementById("select_sport").innerHTML = list;
        });
}

// function filter_data(){
//     let city = document.getElementById("select_city").value;
//     let area = document.getElementById("select_area").value;
//     let sport = document.getElementById("select_sport").value;
//     let url = "http://127.0.0.1:8000/api/ground-list?";
//     if(city != "none"){
//         url = url + "city=" + city + "&";
//     }
//     if(area != "none"){
//         url = url + "area=" + area + "&";
//     }
//     if(sport != "none"){
//         url = url + "sport_name=" + sport + "&";
//     }
//     fetch(url)
//         .then(response => response.text())
//         .then(data => {
//             // let json = JSON.stringify(data);
//             // json = json.replaceAll('\\', '');
//             console.log(data);
//             document.getElementById("display-list").innerHTML = "<p>"+data+"</p>";
//         });
// }

set_city();
set_area();
set_sport();
// filter_data();

