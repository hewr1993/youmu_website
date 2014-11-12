$( document ).ready(function() {
    $.stellar();
});

$(window).load(function() {
    var navpos = $('.navbar').offset();
    console.log(navpos.top);
    $(window).bind('scroll', function() {
        if ($(window).scrollTop() > navpos.top) {
            $('.navbar').addClass('navbar-fixed');
            $('.masthead').addClass('masthead-expanded');
        }
        else {
            $('.navbar').removeClass('navbar-fixed');
            $('.masthead').removeClass('masthead-expanded');
        }
    }); 
});
