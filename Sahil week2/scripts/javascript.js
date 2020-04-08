let myButton = document.getElementById('button1');
let myHeading = document.querySelector('h4');

function setUserName() {
            let myName = prompt('Please login with your name');
            if(!myName || myName === null) {
            setUserName();  
            } else {
            localStorage.setItem('name', myName);
            myHeading.innerHTML = 'Welcome to the website of soccer's most prestigious event, the UEFA Champions League, ' + myName;
            }
         }

if(!localStoage.getItem('name')) {
 setUserName();
}

myButton.onclick = function() {
setUserName();
}