$(document).ready(function(){
	
	$('#login-submit').click(function(){
		
		var user = $('#login-username-input').val();
		var password = $('#login-password-input').val();
		
		$.post('users/login', {'user': user, 'password': password}, function(data){
			var data = data.split(";");
			if (data[0] == "1") {
				
				window.location ='/welcome/'+ data[1];
				
				// REDIRECT TO WELCOME PAGE
				// WELCOME PAGE SHOULD RECEIVE USERNAME AND LOGCOUNT AS A PARAMETER
				// WELCOME PAGE SHOULD REDIRECT THE USER BACK TO THE LOGIN PAGE IF THE USER IS NOT LOGGED IN.
				
			} else {
				if (data[0] == "-1") {
					$('#login-message').text("Invalid username and password combination. Please try again.");
				} else if (data[0] == "-2") {
					$('#login-message').text("This user name already exists. Please try again.");
				} else if (data[0] == "-3") {
					$('#login-message').text("The user name should be non-empty and at most 128 characters long. Please try again.");
				} else if (data[0] == "-4") {
					$('#login-message').text("The password should be at most 128 characters long. Please try again.");
				}
			}
		});
		
	});
	
	$('#login-add').click(function(){
		
		var user = $('#login-username-input').val();
		var password = $('#login-password-input').val();
		
		$.post('users/add', {'user': user, 'password': password}, function(data){
			var data = data.split(";");
			if (data[0] == "1") {
				
				window.location ='/welcome/'+data[1];
				
				// REDIRECT TO WELCOME PAGE
				// WELCOME PAGE SHOULD RECEIVE USERNAME AND LOGCOUNT AS A PARAMETER
				// WELCOME PAGE SHOULD REDIRECT THE USER BACK TO THE LOGIN PAGE IF THE USER IS NOT LOGGED IN.
				
			} else {
				if (data[0] == "-1") {
					$('#login-message').text("Invalid username and password combination. Please try again.");
				} else if (data[0] == "-2") {
					$('#login-message').text("This user name already exists. Please try again.");
				} else if (data[0] == "-3") {
					$('#login-message').text("The user name should be non-empty and at most 128 characters long. Please try again.");
				} else if (data[0] == "-4") {
					$('#login-message').text("The password should be at most 128 characters long. Please try again.");
				}
			}
		});
		
	});
	
	$('#welcome-logout').click(function(){
		window.location = '/';
	});
	
});