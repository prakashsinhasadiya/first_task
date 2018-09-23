$(document).ready(function() {
    $('#example').DataTable();
$("#column_add").click(function () {
      var form = $(this).closest("form");    
      $.ajax({
      	type : "POST",
        url: '/',
        data: form.serialize(),
        success: function (data) {
          debugger;
        },
        error: function (data) {
          debugger;
        },
        
      });

    });
} );
