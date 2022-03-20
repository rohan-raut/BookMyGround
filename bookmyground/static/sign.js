console.clear();

const loginBtn = document.getElementById('login');
const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode.parentNode;
	Array.from(e.target.parentNode.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			signupBtn.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

signupBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode;
	Array.from(e.target.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			loginBtn.parentNode.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});



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
