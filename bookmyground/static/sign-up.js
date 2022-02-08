function validatePassword() {
    var newPassword = document.getElementById('password').value;
    var minNumberofChars = 8;
    var maxNumberofChars = 100;
    let re = new RegExp('^(((?=.[a-z])(?=.[A-Z]))|((?=.[a-z])(?=.[0-9]))|((?=.[A-Z])(?=.[0-9])))(?=.{6,100})');
    // var regularExpression  = /^(((?=.[a-z])(?=.[A-Z]))|((?=.[a-z])(?=.[0-9]))|((?=.[A-Z])(?=.[0-9])))(?=.{6,100})/gm;
    // if(newPassword.length < minNumberofChars || newPassword.length > maxNumberofChars){
    //     alert("Password should have atleast 8 characters");
    //     return false;
    // }
    if(!re.test(newPassword)) {
        alert("Password password should contain atleast one number and one special character");
        return false;
    }
}


function CheckPassword() 
{ 
var passw=  /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
// var passw=  /^\D*$/;
var newPassword = document.getElementById('password').value;
if(passw.test(newPassword)) 
{ 
alert('Correct, try another...')
flag = true;
return true;
}
else
{ 
alert('Wrong...!')
return false;
}
}


// document.getElementById('password').addEventListener("change", ()=>{
//     console.log("running");
// })

// function changed() {
//     console.log("changed");
// }
