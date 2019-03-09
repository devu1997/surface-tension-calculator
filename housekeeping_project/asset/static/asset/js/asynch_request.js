$(document).ready(function() {	
	$('.asynch-request-btn').click(function(){
		var submit_button = $(this);
		var form_container = submit_button.closest('.asynch-request-container');
		var form = form_container.children('.asynch-request-form:first');
		var form_error = form.children('.asynch-request-error:first');
		var form_loader = form_container.children('.asynch-request-loader:first');
		
		submit_button.attr('disabled','disabled');
		form_container.animate({opacity:'.5'});
		form_loader.fadeIn();
		
		var URL = form.attr('action');
		var method = form.attr('method');
		
		$.ajax({
			url:URL,
			type:method,
			dataType:'json',
			success: function(response_data) {
				form_loader.fadeOut();
				form_container.animate({opacity:'1'});
				submit_button.removeAttr('disabled');
				
				if(response_data['success_status']) {
					form_error.text('');
				} else {
					form_error.text(response_data['error_message']);
				}
			},
			error: function(jXHR, textStatus, errorThrown) {
				form_loader.fadeOut();
				form_container.animate({opacity:'1'});
				submit_button.removeAttr('disabled');
				error_container.text(errorThrown);
			}
		})
	});
});