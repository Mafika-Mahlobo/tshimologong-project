$(document).ready( function() {


	var pizza = pasta = pap = other = false;

	$("input[name='pizza']").on("change", function() {

		if ($(this).is(":checked")) {
			pizza = true;
		} else {
			pizza = false;
		}

	});

	$("input[name='pasta']").on("change", function() {

		if ($(this).is(":checked")) {
			pasta = true;
		} else {
			pasta = false;
		}

	});

	$("input[name='pap']").on("change", function() {

		if ($(this).is(":checked")) {
			pap = true;
		} else {
			pap = false;
		}

	});

	$("input[name='other']").on("change", function() {

		if ($(this).is(":checked")) {
			other = true;
		} else {
			other = false;
		}

	});


	function checkAge(dateStr) {
    	
    	var birthDate = new Date(dateStr);
    
    	// Get the current date
    	var currentDate = new Date();
    
    	// Calculate the difference in milliseconds between the current date and birth date
    	var dateDifference = currentDate - birthDate;
    
    	// Convert milliseconds to years (approximately)
    	var age = Math.floor(dateDifference / (1000 * 60 * 60 * 24 * 365));
    
    	return age;
   	}

   	$("input[name='date']").on("input", function() {
   		const date = $(this).val();
   		const age = checkAge(date);

   		if (age < 5 || age > 120) {
   			alert("You must be over 5 year old, and younger than 120 years!");
   			location.reload();
   		} else {
   			$("#date_value").val(age);
   		}


   	});


});
	
