

select_city = "<option value='--Select--'>--Select--</option>";
let i = 0;
for (i = 0; i < json_obj['city'].length; i++) {
    select_city = select_city + "<option value='" + json_obj['city'][i] + "'>" + json_obj['city'][i] + "</option>\n";
}
document.getElementById("select_city").innerHTML = select_city;


select_area = "<option value='--Select--'>--Select--</option>";
i = 0;
for (i = 0; i < json_obj['area'].length; i++) {
    select_area = select_area + "<option value='" + json_obj['area'][i] + "'>" + json_obj['area'][i] + "</option>\n";
}
document.getElementById("select_area").innerHTML = select_area;

select_sport = "<option value='--Select--'>--Select--</option>";
i = 0;
for (i = 0; i < json_obj['sport'].length; i++) {
    select_sport = select_sport + "<option value='" + json_obj['sport'][i] + "'>" + json_obj['sport'][i] + "</option>\n";
}
document.getElementById("select_sport").innerHTML = select_sport;

// filtering starts here 

function set_city() {
    let city = document.getElementById("select_city").value;
    let area = document.getElementById("select_area").value;
    console.log(city);


    select_area = "<option value='--Select--'>--Select--</option>";
    i = 0;
    for (i = 0; i < json_obj[city].length; i++) {
        select_area = select_area + "<option value='" + json_obj[city][i] + "'>" + json_obj[city][i] + "</option>\n";
    }
    document.getElementById("select_area").innerHTML = select_area;

    if (city == "--Select--") {
        select_area = "<option value='--Select--'>--Select--</option>";
        i = 0;
        for (i = 0; i < json_obj['area'].length; i++) {
            select_area = select_area + "<option value='" + json_obj['area'][i] + "'>" + json_obj['area'][i] + "</option>\n";
        }
        document.getElementById("select_area").innerHTML = select_area;
    }
}