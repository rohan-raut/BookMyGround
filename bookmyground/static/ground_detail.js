from_time = from_time.split(":")[0] + ":" + from_time.split(":")[1];
to_time = to_time.split(":")[0] + ":" + to_time.split(":")[1];

function today_timeslot() {
    var today = new Date();
    var day = String(today.getDate()).padStart(2, '0');
    var month = String(today.getMonth() + 1).padStart(2, '0');
    var year = today.getFullYear();
    today = year + '-' + month + '-' + day;

    // getting total slots in set 
    let total_slots = new Set();
    let from_time_int = parseInt(from_time.split(":")[0]);
    let to_time_int = parseInt(to_time.split(":")[0]);
    for (let i = from_time_int; i < to_time_int; i++) {
        prepended_number = String(i).padStart(2, '0');
        slot = prepended_number + ":00";
        total_slots.add(slot);  
    }

    // getting booked slots in set 
    let booked_slots = new Set();
    let available_slots = new Set();
    api = "http://" + hostname + ":" + port + "/api/booking?ground_id=" + pk + "&date=" + today;
    fetch(api)
        .then(response => response.text())
        .then(data => {
            let json = JSON.parse(data);
            json.forEach(obj => {
                let slot = obj.from_time.split(":")[0] + ":" + obj.from_time.split(":")[1]
                booked_slots.add(slot);
            });
            available_slots = total_slots;
            booked_slots.forEach(element => {
                available_slots.delete(element);
            });
            available_slots_range = new Set();
            available_slots.forEach(element => {
                time1_int = parseInt(element.split(":")[0]);
                time2_int = time1_int + 1;
                time1_str = String(time1_int).padStart(2, '0');
                time2_str = String(time2_int).padStart(2, '0');
                range = time1_str + ":00" + " to " + time2_str + ":00";
                available_slots_range.add(range);
            });
            console.log(available_slots_range);
        });

    

}

today_timeslot();

function get_slots() {
    date = document.getElementById('date').value;
    console.log(date);

    // getting total slots in set 
    let total_slots = new Set();
    let from_time_int = parseInt(from_time.split(":")[0]);
    let to_time_int = parseInt(to_time.split(":")[0]);
    for (let i = from_time_int; i < to_time_int; i++) {
        prepended_number = String(i).padStart(2, '0');
        slot = prepended_number + ":00";
        total_slots.add(slot);  
    }

    let booked_slots = new Set();
    let available_slots = new Set();
    api = "http://" + hostname + ":" + port + "/api/booking?ground_id=" + pk + "&date=" + date;
    fetch(api)
        .then(response => response.text())
        .then(data => {
            let json = JSON.parse(data);
            json.forEach(obj => {
                let slot = obj.from_time.split(":")[0] + ":" + obj.from_time.split(":")[1]
                booked_slots.add(slot);
            });
            available_slots = total_slots;
            booked_slots.forEach(element => {
                available_slots.delete(element);
            });
            available_slots_range = new Set();
            available_slots.forEach(element => {
                time1_int = parseInt(element.split(":")[0]);
                time2_int = time1_int + 1;
                time1_str = String(time1_int).padStart(2, '0');
                time2_str = String(time2_int).padStart(2, '0');
                range = time1_str + ":00" + " to " + time2_str + ":00";
                available_slots_range.add(range);
            });
            console.log("available slots on "+date);
            console.log(available_slots_range);
        });
}
