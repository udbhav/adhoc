$(document).ready(function() {
  // serve ads
  $.post("/ads/serve/", {slots: "[1, 2, 3]"}, function(data) {
    for (i=0;i<data.length;i++) {
      
      $("#ad_slot_" + data[i]['slot']).html(data[i]['code']).addClass("inserted");
    }
  });

});
