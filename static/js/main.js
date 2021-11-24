
//Alert Messages' FadeOut

window.setTimeout(function() {
    $(".alert-dismissible").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
}, 5000);

//Navbar
jQuery(function($) {
    $(window).on('scroll', function() {
		if ($(this).scrollTop() >= 1) {
			$('.navbar').addClass('fixed-top');
		} else if ($(this).scrollTop() === 0) {
			$('.navbar').removeClass('fixed-top');
		}
	});

	function adjustNav() {
		var winWidth = $(window).width(),
			dropdown = $('.dropdown'),
			dropdownMenu = $('.dropdown-menu');

		if (winWidth >= 768) {
			dropdown.on('mouseenter', function() {
				$(this).addClass('show')
					.children(dropdownMenu).addClass('show');
			});

			dropdown.on('mouseleave', function() {
				$(this).removeClass('show')
					.children(dropdownMenu).removeClass('show');
			});
		} else {
			dropdown.off('mouseenter mouseleave');
		}
	}

	$(window).on('resize', adjustNav);

	adjustNav();
});
