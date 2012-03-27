$(document).ready(function() {
	$body = $("body");
	
	function animate() {
		
		$body.animateGradient('linear-gradient(purple, orange)', 1000);
		$body.animateGradient('linear-gradient(green, pink)', 1000);
		$body.animateGradient('linear-gradient(blue, green)', 1000);
		
		setTimeout(function(){
			animate()
		}, 1000);
	}

	function radialAnimate() {
	
		$body.animateGradient('radial-gradient(40% 50%, circle, purple, orange)', 1000);
		$body.animateGradient('radial-gradient(40% 50%, circle, green, pink)', 1000);
		$body.animateGradient('radial-gradient(40% 50%, circle, blue, green)', 1000);
		
		setTimeout(function(){
			radialAnimate()
		}, 1000);
	}	
	//animate();
	
	radialAnimate();

});