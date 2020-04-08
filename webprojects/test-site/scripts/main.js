let myImage= document.querySelector('img');

myImage.onclick= function(){
	let mySrc = myImage.getAttribute('src');
	if(mySrc === 'images/horseicon.jpg'){
		myImage.setAttribute('src','images/bulb.png');
	}else{
		myImage.setAttribute ('src','images/horseicon.jpg');
	}
}
let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');
function setUsername(){
	let myName = prompt('Please enter your name.');
	if(!myName || myName === null){
		setUsername();
	}else{
	localStorage.setItem('name', myName);
	myHeading.textContent = 'Welcome to Illuminati ' + myName +' !';
	}
}
if(!localStorage.getItem('name')){
	setUsername();
}else{
	let storedName = localStorage.getItem('name');
	myHeading.textContent = 'Welcome to Illuminati '+ storedName + ' !';
}
myButton.onclick = function(){
	setUsername();
}
