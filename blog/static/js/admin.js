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

});


