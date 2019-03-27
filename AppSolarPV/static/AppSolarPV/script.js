/*
	Anil Patel
	IFT 458 Spring C 2019
	script.js
*/

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
		} 
		else {
			alert("Geolocation is not supported by this browser.");
			}
}

function validateForm() {
	var uN = document.forms["registration"]["uName"].value;
	if (uN == "") {
		alert("Username must be filled out");
		return false;

		}
}