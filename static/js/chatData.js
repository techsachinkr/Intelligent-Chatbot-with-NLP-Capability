(function($) {
    $.fn.onEnter = function(func) {
        this.bind('keypress', function(e) {
            if (e.keyCode == 13) func.apply(this, [e]);    
        });               
        return this; 
     };
})(jQuery);

$( function () {
    console.log($("input"));
    $("input").onEnter( function() {
        $.ajax({
			type: 'POST',
			url: '/getChatData',
			data: $('form').serialize()+'inputChat='+$("input").val(),
			success: function(response){
                dataVal= $.parseJSON(response)
				$( "#chatWindow" ).append("<p style='color:blue;'>User Said: "+dataVal.UserInput+"</p><br>");				
				$( "#chatWindow" ).append("<p style='color:green;'>BotResponse:  Your question is related to. "+dataVal.InputCategory+"<br>For Detailed step-by-step info you can goto:<br> "+dataVal.BotResponse+"<br> What else i can help you with now ?</p><br>");
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});                    
    });
});