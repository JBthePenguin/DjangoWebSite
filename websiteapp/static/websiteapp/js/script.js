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
        window.location.href = window.location.href;
      },
      error: function(data) {
        alert(data);
      },
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
        window.location.href = window.location.href;
      },
      error: function(data) {
        alert(data);
      },
    });
  });
});
