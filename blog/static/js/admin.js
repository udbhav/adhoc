$(document).ready(function() {
  if (!navigator.userAgent.match(/(iPhone|iPod|iPad|BlackBerry|Android)/)) {
    $("textarea").ckeditor({
			  toolbar :
			  [
            {name: 'basic', items : ['Bold', 'Italic', '-', 'Link', 'Unlink','-', 'Image', 'Blockquote'] },
	          { name: 'clipboard', items : [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo', 'Source' ] },
			  ],
        filebrowserBrowseUrl : '/images/',
        filebrowserUploadUrl : '/images/new/'
    });
  }

  // Only do this if we're adding a new one
  if (document.location.pathname.indexOf('add') != -1) {
    // select the right author
    $("select#id_author option[selected]").removeAttr("selected");
    $("select#id_author option[value=" + user_id + "]").attr("selected", "selected");
  }
});


