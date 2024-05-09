$(document).ready( function() {

	function personal() {
		const name = $("input[name='fullname']");
		const email = $("input[name='email']");
		const date = $("input[name='date']");
		const phone = $("input[name='phone_number']");

		//return all values (json or array)
	}
	

	function preferences(){
		const pizza = $("input[name='pizza']");
		const pasta = $("input[name='pasta']");
		const pap = $("input[name='pap']");
		const other = $("input[name='other']");

		//return all values (json or array)
	}

	function ratings() {
		const movie = $("input[name='movie']:checked");
		const radio = $("input[name='radio']:checked");
		const eat = $("input[name='eat']:checked");
		const tv = $("input[name='tv']:checked");

		//return all values (json or array)
	}

	function getAge() {
		//get and validate age here
	}

	function submit() {
		//submit on button click
	}

	
	$(".submit-button").click(function(){

		const a = personal();
		const b = preferences();
		const c = ratings();

		if (a.val() === "") {
			alert("No value provided");
		} else {
			alert(a.val());
		}

		if (b.prop("checked")) {
			b.val(true);
		} else {
			b.val(false);
		}

		alert(b.val());

		if (c.length < 1){
			alert("Complete rating!");
		} else {
			alert(c.val());
		}	
	});
});
	
