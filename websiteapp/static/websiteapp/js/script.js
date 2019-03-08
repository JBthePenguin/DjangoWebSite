// FOOTER
// Check buttons
$(document).ready(function() {
  // Theme
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
        if(location.href.includes("#")) {
          url = location.href.split('#')[0];
          window.location.href = window.url;
        } else {
          window.location.href = window.location.href;
        }
      },
      error: function(data) {
        alert(data);
      },
    });
  });
  // Language
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
        if(location.href.includes("#")) {
          url = location.href.split('#')[0];
          window.location.href = window.url;
        } else {
          window.location.href = window.location.href;
        }
      },
      error: function(data) {
        alert(data);
      },
    });
  });
});
