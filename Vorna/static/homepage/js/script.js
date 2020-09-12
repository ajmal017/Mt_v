$(function() {
	var dict = {
<<<<<<< HEAD
		"row1": "https://www.markettime.ir/update/EURtoUSD/latest/",
		"row2": "https://www.markettime.ir/update/GBPtoUSD/latest/",
		"row3": "https://www.markettime.ir/update/AUDtoUSD/latest/",
		"row4": "https://www.markettime.ir/update/USDtoCAD/latest/",
		"row5": "https://www.markettime.ir/update/USDtoJPY/latest/",
		"row6": "https://www.markettime.ir/update/USDtoINR/latest/",
		"row7": "https://www.markettime.ir/update/USDtoTRY/latest/",
		"row8": "https://www.markettime.ir/update/USDtoCNY/latest/",
		"row9": "https://www.markettime.ir/update/USDtoRUB/latest/",
		"row10": "https://www.markettime.ir/update/USDtoAED/latest/"
=======
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
>>>>>>> 1305fa370dc34ac19282cb50a3176247a9956bb9
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
