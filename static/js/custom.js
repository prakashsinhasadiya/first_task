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
                addrowvalue.push(
                '<button id="column_update" class="btn btn-primary btn-sm"><i class="glyphicon glyphicon-edit" aria-hidden="true">Edit</i></button>');
                addrowvalue.push(
                  '<button id="column_delete" class="btn btn-primary btn-sm"><i class="glyphicon glyphicon-remove" aria-hidden="true">Delete</i></button>');

                debugger;
                table.row.add(addrowvalue).draw();

        }else{
             $(general_errors).after().text(response['response']);
          debugger;

        }
        
        },
        
      });

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