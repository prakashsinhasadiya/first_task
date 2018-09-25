$(document).ready(function() {
    $('#example').DataTable();

  $("#column_add").click(function (event) {
    event.preventDefault();
    if (!$("#column_add").data("attr")){
      var form = $(this).closest("form");
        debugger
      $.ajax({
            url: "/",
            type: "POST",
            data: $(this).closest('form').serialize(),            
            dataType: 'json',
        success: function (response) {
          if (response['status'] == 'success'){
                var table = $('#example').DataTable();

                var addrowvalue = [];
                var result = JSON.parse(response['response']);

                addrowvalue.push(result['name']);
                addrowvalue.push(result['email']);
                addrowvalue.push(result['mobile']);
                addrowvalue.push(result['address']);
                addrowvalue.push(result['dob']);
                addrowvalue.push(result['gender']);
                addrowvalue.push(result['blood_group']);
                var record_id = result['id']
                addrowvalue.push(
                '<button id="'+record_id+'_edit" data-attr="'+record_id+'" class="btn btn-primary btn-sm btn-edit"><i class="glyphicon glyphicon-edit" aria-hidden="true">Edit</i></button>');
                addrowvalue.push(
                  '<button id="'+record_id+'_delete" data-attr="'+record_id+'" class="btn btn-primary btn-sm btn-dlt"><i class="glyphicon glyphicon-remove" aria-hidden="true">Delete</i></button>');
                table.row.add(addrowvalue).node().id = record_id +'_row';
                table.draw( false );
        }else{
             $(general_errors).after().text(response['response']);

        }
        
        },
        
      });
     }else if($("#column_add").data("attr")){
                result = $(this).closest('form').serialize()
                result_rcrd = {'record_id':$("#column_add").data("attr")}

/*                result = {'record_id':$("#column_add").data("attr"),$(this).serialize()}
*/                
                 $.ajax({ // create an AJAX call...
                    data: result,// get the form data
                    type: "POST",
                    dataType:'JSON', // GET or POST
                    url: /edit/, // the file to call
                    success: function(response) {
                      if (response['status'] == 'success'){
                        var table = $('#example').DataTable();
                        var result = JSON.parse(response['response']);
                        var record_id = result['default_user_id'];
                        var row_id = + record_id + "_row";
                        table.row(row_id).remove().draw( false );
                        var addrowvalue = [];
                        debugger
                        addrowvalue.push(result['name']);
                        addrowvalue.push(result['email']);
                        addrowvalue.push(result['mobile']);
                        addrowvalue.push(result['address']);
                        addrowvalue.push(result['dob']);
                        addrowvalue.push(result['gender']);
                        addrowvalue.push(result['blood_group']);
                        var record_id = result['default_user_id']
                        addrowvalue.push(
                          '<button id="'+record_id+'_edit" data-attr="'+record_id+'" class="btn btn-primary btn-sm btn-edit"><i class="glyphicon glyphicon-edit" aria-hidden="true">Edit</i></button>');
                        addrowvalue.push(
                        '<button id="'+record_id+'_delete" data-attr="'+record_id+'" class="btn btn-primary btn-sm btn-dlt"><i class="glyphicon glyphicon-remove" aria-hidden="true">Delete</i></button>');
                        table.row.add(addrowvalue).node().id = record_id +'_row';
                        table.draw( false );
        }else{
             $(general_errors).after().text(response['response']);

        }
                      debugger;
                     
                     }
                });
            }else{}
            return false;
          });




$(document.body).on("click",".btn-dlt", function (event) {
    event.preventDefault();
    if (confirm('Are you sure you want to delete this record?')){
      var form = $(this).closest("form");
      value = {"id":$(this).data("attr"),"row_id":$(this).parent().parent().attr('id')}
      $.ajax({
            url: "/delete/",
            type: "POST",
            data: value,
            dataType: 'JSON',
        success: function (response) {
          if (response['status'] == 'success'){

                var table = $('#example').DataTable();

                var result = JSON.parse(response['response']);
                var record_id = result['id']
                var row_id = '#'+result['row_id']
                table.row(row_id).remove().draw( false );

        }else{
             $(general_errors).after().text(response['response']);

        }

        },
        
      });
    }
    return false;
    });

$(document.body).on("click",".btn-edit", function (event) {
    event.preventDefault();
    var table = $('#example').DataTable();
    var data = table.row($(this).parent().parent()).data();
    debugger;
     $("#name").val(data[0]);
     $("#address").val(data[3]);
     $("#mobile").val(data[2]);
     $("#email").val(data[1]);
     $("#dob").val(data[4]);
     $("#gender").val(data[5]);
     $("#blood_group").val(data[6]);
     $("#user_id").val($(this).data("attr"));
     $("#column_add").html("Update");
     $("#column_add").data("attr", $(this).data("attr"))
    });
} );

