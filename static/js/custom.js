$(document).ready(function() {
    $('#example').DataTable();

$("#column_add").click(function (event) {
  debugger;
    event.preventDefault();
      var form = $(this).closest("form");
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

                var rowIndex = table.fnAddData(addrowvalue);
                var row = table.fnGetNodes(rowIndex);
                $(row).attr( 'id', 'MyUniqueID' );
                debugger;
/*                table.row.add(addrowvalue).draw();
*/
        }else{
             $(general_errors).after().text(response['response']);

        }
        
        },
        
      });

    });
$(".btn-dlt").click(function (event) {
    event.preventDefault();
    if (confirm('Are you sure you want to delete this record?')){
      var form = $(this).closest("form");
      debugger
      value = {"id":$(this).data("attr"),"row_id":this.id}
      $.ajax({
            url: "/delete/",
            type: "POST",
            data: value,
            dataType: 'json',
        success: function (response) {
          if (response['status'] == 'success'){

                var table = $('#example').DataTable();

                var addrowvalue = [];
                var result = JSON.parse(response['response']);
                var record_id = result['id']
                var row_id = '#'+result['row_id']
                  debugger;
                table.row(row_id).remove().draw( false );

        }else{
             $(general_errors).after().text(response['response']);

        }

        },
        
      });
    }
    return false;
    });
} );



/*
            if (response['status']=='success'){
                var table = $('#profile_details_table').DataTable();

                debugger
                var value_list = [];

                value_list.push(response['name']);
                value_list.push(response['email']);
                value_list.push(response['mobile']);
                value_list.push(response['address']);
                value_list.push(response['gender']);
                value_list.push(response['user_dob']);
                value_list.push(response['blood_group']);

                $('#profile_details_table').DataTable().row.add( value_list ).draw();

            }else{

                var form_input = $("form#user_detail_form :input");

                var required_fields = [];

                for(var i=0; i<form_input.length; i++){
                    if (JSON.parse(response['response'])[form_input[i].name]){
                        required_fields.push(i);
                    }
                }

                for(var j=0; j<required_fields.length; j++){


                    var input_field = form_input[required_fields[j]];

                    
                    var error_msg = JSON.parse(response['response'])[input_field.name];

                    $(input_field).css({'border-color': 'red'});

                    $(input_field).next().text(error_msg);
                }

            }
        }
    });

});*/