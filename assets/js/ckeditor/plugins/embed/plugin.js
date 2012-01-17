CKEDITOR.plugins.add(
    'embed',
    {
	      init: function( editor )
	      {
            editor.addCommand(
                'insertTimestamp',
	              {
		                exec : function( editor )
		                {    
                        var link = prompt('Embed URL', 'http://');
			                  editor.insertHtml('<a href="' + link + '" class="oembed">' + link + '</a>');
		                }
	              });

            editor.ui.addButton( 'Timestamp',
                                 {
	                                   label: 'Insert Timestamp',
	                                   command: 'insertTimestamp',
	                                   icon: this.path + 'images/timestamp.png'
                                 } );
	      }
    }
);
