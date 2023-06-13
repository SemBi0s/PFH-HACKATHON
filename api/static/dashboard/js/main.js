var countDownDate = new Date("Jun 19, 2023 16:00:00").getTime();
var countDownDateTwo = new Date("Jun 20, 2023 16:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;
  var distance2 = countDownDateTwo - now;

  // Time calculations for days, hours, minutes and seconds
  

  if (distance < 0) {
    document.getElementById("timer-container").innerHTML = '<h2 class="timer-title"> Hackathon end in :</h2> ';
    var [days, hours, minutes,seconds] = getdistance(distance2);
    document.getElementById("timer-container").innerHTML += '<h1 class="timer">' + days + "d " + hours + "h "+ minutes + "m " + seconds + "s " + '</h1>';
  }else if (distance2 < 0){
  	clearInterval(x)
 	  document.getElementById("timer-container").innerHTML = "The Hackathon ended";
  }
  else{
  	document.getElementById("timer-container").innerHTML = '<h2 class="timer-title"> Hackathon start in :</h2> ';
  	var [days, hours, minutes, seconds] = getdistance(distance);
  	document.getElementById("timer-container").innerHTML += '<h1 class="timer">' + days + "d " + hours + "h "+ minutes + "m " + seconds + "s " + '</h1>';
  }
  // Display the result in the element with id="demo"
  

  // If the count down is finished, write some text
}, 1000);

function getdistance(distance){
	  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
	  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  	var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  	var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  	return [days,hours,minutes,seconds];
}