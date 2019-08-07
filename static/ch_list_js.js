$( document ).ready(function() {
	console.log("suk dik");
    var count = 8;
	var redirect = "https://www.apphp.com";
	 
	function countDown(){
	    var timer = document.getElementById("timer");
	    while(count > 0){
	    	console.log(count)
	        count--;
	        $(".re").html("Redirecting in " + count);
	        timer.innerHTML = "This page will redirect in "+count+" seconds.";
	        setTimeout("countDown()", 1000);
	    }
	    window.location.href = redirect;
	}

	// countDown();
	window.onbeforeunload = function(e) {
		console.log("shit");
		location.href = 'http://domain.tld/gettingstarted.html';
	};
});