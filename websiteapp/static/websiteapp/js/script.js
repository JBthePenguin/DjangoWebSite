// NAVBAR

// Wave effect
(function ($) {
  var SCROLLING_NAVBAR_OFFSET_TOP = 50;
  $(window).on('scroll', function () {
    var $navbar = $('.navbar');
    if ($navbar.length) {
      if ($navbar.offset().top > SCROLLING_NAVBAR_OFFSET_TOP) {
        $('.scrolling-navbar').addClass('top-nav-collapse');
      } else {
        $('.scrolling-navbar').removeClass('top-nav-collapse');
      }
    }
  });
})(jQuery);

// Theme
$(document).ready(function() {
  $("#theme-check").change(function() {
    if(this.checked) {
        url_theme = "/change_theme/dark/";
    } else {
        url_theme = "/change_theme/light/";
    }
    $.ajax({
      type: 'GET',
      url: url_theme,
      success: function(data) {
        location.reload();
      }
    });
  });
});
