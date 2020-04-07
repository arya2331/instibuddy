let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/pic1.jpg') {
      myImage.setAttribute ('src','images/pic2.jpg');
    } else {
      myImage.setAttribute ('src','images/pic1.jpg');
    }
}
let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

function setUserName() {
  let myName = prompt('Please enter your name.');
  localStorage.setItem('name', myName);
  myHeading.textContent = 'Hey, This is my first website! ' + myName;
}


if(!localStorage.getItem('name')) {
  setUserName();
} else {
  let storedName = localStorage.getItem('name');
  myHeading.textContent = 'Hey, This is my first website! ' + storedName;
}

myButton.onclick = function() {
  setUserName();
}
function setUserName() {
  let myName = prompt('Hello! Please enter your name.');
  if(!myName || myName === null) {
    setUserName();
  } else {
    localStorage.setItem('name', myName);
    myHeading.innerHTML = 'Hey, This is my first website! ' + myName;
  }
}