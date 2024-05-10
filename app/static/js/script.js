$(document).ready( function() {

	$('.submit-button').prop('disabled', true);

	$("input[name='date']").on("input", function() {
		if ($(this).val().trim() !== '') {

            $('.submit-button').prop('disabled', false);
        } else {
            $('.submit-button').prop('disabled', true);
        }
	});

	const personal = async () => {
		const name = $("input[name='fullname']");
		const email = $("input[name='email']");
		const date = $("input[name='date']");
		const phone = $("input[name='phone_number']");
		try {
			const age = await getAge(date); 
			return age; 
		} catch (error) {
			console.error("Error:", error);
			return null; 
		}
	}

	async function getAge(date) {
		return new Promise((resolve, reject) => {
			$.ajax({
				url: "/compute_age",
				type: "POST",
				contentType: "application/json",
				data: 	JSON.stringify({date: date.val()}),
				success: function(age) {
					resolve(age);
				},
				error: function(xhr, status, error) {
					reject(error);
				}
			});
		});
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

	function submit() {
		//submit on button click
	}

	
	$(".submit-button").click(function(){

		const a = personal().then(age => {
			alert(age.age);
		});


		//alert(a.val());
		// const b = preferences();
		// const c = ratings();

		// if (a.val() === "") {
		// 	alert("No value provided");
		// } else {
		// 	alert(a.val());
		// }

		// if (b.prop("checked")) {
		// 	b.val(true);
		// } else {
		// 	b.val(false);
		// }

		// alert(b.val());

		// if (c.length < 1){
		// 	alert("Complete rating!");
		// } else {
		// 	alert(c.val());
		// }	
	});
});
	
