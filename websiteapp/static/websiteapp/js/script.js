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


// FOOTER

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

// Language
$(document).ready(function() {
  $("#lang-check").change(function() {
    if(this.checked) {
        url_lang = "/change_lang/fr/";
    } else {
        url_lang = "/change_lang/en/";
    }
    $.ajax({
      type: 'GET',
      url: url_lang,
      success: function(data) {
        location.reload();
      }
    });
  });
});
