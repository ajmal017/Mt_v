$(function() {
	var dict = {
		"row1": "EURUSD",
		"row2": "GBPUSD",
		"row3": "AUDUSD",
		"row4": "USDCAD",
		"row5": "USDJPY",
		"row6": "USDINR",
		"row7": "USDTRY",
		"row8": "USDCNY",
		"row9": "USDRUB",
		"row10": "USDAED"
	};


	$("[name='price']").each(function(){
			var ad = "https://www.markettime.ir/update/CurrencyExchange/"
			// dict[$(this).attr("value")]
			var el = $(this)
			var t = $(this).text()
			$.ajax({
				url: ad,
				type: 'GET',
				async: true,
				dataType: 'json',
				success:function(data){
					console.log(data)
					$.each(data, function(index, json){

					})
					var after = parseFloat(data.rate).toFixed(4);
					el.text(after);
				}
			});
		});


	setInterval(function(){
		var ad = "https://www.markettime.ir/update/CurrencyExchange/"
		// dict[$(this).attr("value")]
		$.ajax({
			url: ad,
			type: 'GET',
			async: true,
			success:function(data){

			}
		});
		$("[name='price']").each(function(){
			var ad = "https://www.markettime.ir/update/CurrencyExchange/"
			var el = $(this)
			var t = $(this).text()
			$.ajax({
				url: ad,
				type: 'GET',
				async: true,
				success:function(data){
					var after = parseFloat(data.rate).toFixed(4);
					var before = parseFloat(t).toFixed(4);
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
					el.text(after);
				}
			});
		});
	}, 3000);
})
