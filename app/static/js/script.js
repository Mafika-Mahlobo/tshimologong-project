$(document).ready( function() {

	function personal() {
		const name = $("input[name='fullname']");
		const email = $("input[name='email']");
		const date = $("input[name='date']");
		const phone = $("input[name='phone_number']");

		return date;
	}
	

	function preferences(){
		const pizza = $("input[name='pizza']");
		const pasta = $("input[name='pasta']");
		const pap = $("input[name='pap']");
		const other = $("input[name='other']");

		return other;
	}

	function ratings() {
		const movie = $("input[name='movie']:checked");
		const radio = $("input[name='radio']:checked");
		const eat = $("input[name='eat']:checked");
		const tv = $("input[name='tv']:checked");

		return movie;
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

		if (a.prop("checked")) {
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
	
