//Initiate jQuery on load.
$(function() {
  //Translate text with flask route
  $("#translate").on("click", function(e) {
    e.preventDefault();
    var translateVal = document.getElementById("text-to-translate").value;
    var translateRequest = { 'text': translateVal}

    if (translateVal !== "") {
      $.ajax({
        url: 'https://engurd.onrender.com/translate-text',
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        dataType: 'json',
        data: JSON.stringify(translateRequest),
        success: function(data) {
          for (var i = 0; i < data.length; i++) {
			  if(i>0)
			  {
				  document.getElementById("translation-result").value += "\\n" + data[i];
			  } 
			  else{
				  document.getElementById("translation-result").value = data[i];
			  }
		  }
        }
      });
    };
  });
  
})
