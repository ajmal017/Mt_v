$(function() {
	var dict = {
		"row1": "https://195.114.8.222/update/EURtoUSD/latest/",
		"row2": "https://195.114.8.222/update/GBPtoUSD/latest/",
		"row3": "https://195.114.8.222/update/AUDtoUSD/latest/",
		"row4": "https://195.114.8.222/update/USDtoCAD/latest/",
		"row5": "https://195.114.8.222/update/USDtoJPY/latest/",
		"row6": "https://195.114.8.222/update/USDtoINR/latest/",
		"row7": "https://195.114.8.222/update/USDtoTRY/latest/",
		"row8": "https://195.114.8.222/update/USDtoCNY/latest/",
		"row9": "https://195.114.8.222/update/USDtoRUB/latest/",
		"row10": "https://195.114.8.222/update/USDtoAED/latest/"
	};
	
	
	$("[name='price']").each(function(){
			var ad = dict[$(this).attr("value")]
			var el = $(this)
			var t = $(this).text()
			$.ajax({
				url: ad,
				type: 'GET',
				async: true,
				success:function(data){
					var after = parseFloat(data.rate).toFixed(4);
					el.text(after);
				}
			});
		});
	
	
	setInterval(function(){
		$("[name='price']").each(function(){
			var ad = dict[$(this).attr("value")]
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