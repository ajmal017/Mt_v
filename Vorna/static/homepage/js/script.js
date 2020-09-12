$(function() {
		$.ajax({
			url: "https://www.markettime.ir/update/CurrencyExchange/latest",
			type: 'GET',
			async: true,
			dataType: 'json',
			success:function(data){
				$.each(data, function(key,value) {
					var el = $("#"+key);
					var after = parseFloat(value).toFixed(4);
					var before = parseFloat(el.text()).toFixed(4);
					$("#" + key).text(after);
					if (before != after) {
						var sign = "";
						if (after > before){
							sign = "+";
							el.animate({
								color: "green"
							}, 1000, function(){
								el.animate({
									color: "white"
								}, 1000)
							})

						} else {
							sign = "-";
							el.animate({
								color: "red"
							}, 1000, function(){
								el.animate({
									color: "white"
								}, 1000)
							})
						}
						var changed = parseFloat(Math.abs(after-before)).toFixed(4)
						el.next().next().text(changed+sign)
					}
				})
			}
		});

	setInterval(function(){
		$.ajax({
			url: "https://www.markettime.ir/update/CurrencyExchange/latest",
			type: 'GET',
			async: true,
			dataType: 'json',
			success:function(data){
				$.each(data, function(key,value) {
					var el = $("#"+key);
					var after = parseFloat(value).toFixed(4);
					var before = parseFloat(el.text()).toFixed(4);
					$("#" + key).text(after);
					if (before != after) {
						var sign = "";
						if (after > before){
							sign = "+";
							el.animate({
								color: "green"
							}, 1000, function(){
								el.animate({
									color: "white"
								}, 1000)
							})

						} else {
							sign = "-";
							el.animate({
								color: "red"
							}, 1000, function(){
								el.animate({
									color: "white"
								}, 1000)
							})
						}
						var changed = parseFloat(Math.abs(after-before)).toFixed(4)
						el.next().next().text(changed+sign)
					}
			})
		}
	});
	}, 3000);
})
