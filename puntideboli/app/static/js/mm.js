function poll() {
	$.ajax({
    	url: '/pwd',
    	dataType: 'json',
    	type: 'get',
    	success: function(data) { // check if available
      		if(data) { // get and check data value
      			$("#status").empty();
      			data.forEach(function(creds) {
    				aux = $("#status").append('<div class="alert alert-danger" role="alert">' + creds[0] + " / " + creds[1] + '</div>');
    				// aux.text(creds[0] + " / " + creds[1]);
    			})
      		}
    	},
    	error: function(error) {
      		console.log(error);
      	}
    });
}

window.onload = function() {
	pollInterval = setInterval(function() {
  		poll();
  	}, 2000);
	poll();
}