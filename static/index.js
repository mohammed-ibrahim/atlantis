function openInNewTab(url) {
    var win = window.open(url, '_blank');
    win.focus();
}

function showModal() {
    $('.ui.modal').modal('show');
}

Handlebars.registerHelper('htmlize', function(object) {
  var text = Handlebars.escapeExpression(object);

  return new Handlebars.SafeString(text.replace(new RegExp("\n", "g"), "<br/>"));
});

// Handlebars.registerHelper('datehelper', function(object) {
//
//     if (!object) {
//         return '';
//     }
//
//   var text = Handlebars.escapeExpression(object);
//
//   return new Handlebars.SafeString(text.replace(new RegExp("\n", "g"), "<br/>"));
// });

// window.onload = function() {
//   //Grab the inline template
//   var template = document.getElementById('template').innerHTML;
//
//   //Compile the template
//   var compiled_template = Handlebars.compile(template);
//
//   //Render the data into the template
//   var rendered = compiled_template({name: "Test Name", power: "Test text"});
//
//   //Overwrite the contents of #target with the renderer HTML
//   document.getElementById('content-placeholder').innerHTML = rendered;
// }


$(function () {
    // // Grab the template script
    // var theTemplateScript = $("#address-template").html();
    // // console.log(theTemplateScript);
    //
    // // Compile the template
    // var theTemplate = Handlebars.compile(theTemplateScript);
    //
    // // Define our data object
    // var gcc1 = {
    //     "city": "London",
    //     "street": "Baker Street",
    //     "number": "221B"
    // };
    //
    // // Pass our data to the template
    // var theCompiledHtml = theTemplate(gcc1);
    // console.log(theCompiledHtml);
    //
    // // Add the compiled html to the page
    // $('.content-placeholder').html(theCompiledHtml);


    // $('.inplace').inplace({ cancelClass:   'inplace__cancel btn btn-danger',fieldClass:    'inplace__field form-control',saveClass:     'inplace__save btn btn-primary' });
    loadPrimaryPage();
});

function loadPrimaryPage() {
    $.ajax({
        type: 'GET',
        url: getAllTasksApi(),
        dataType: 'json',
        success: function (data) {

            console.log("Loading primary page");
            var source = $("#table-data-template").html();
            var template = Handlebars.compile(source);
            $('#primary-tasks-table-body').html(template(data));
            $('.ui.calendar').calendar({
              type: 'date',
              formatter: {
                  date: function (date, settings) {
                      if (!date) return '';
                      var day = date.getDate();
                      var month = date.getMonth() + 1;
                      var year = date.getFullYear();
                      return year + '-' + month + '-' + day;
                  }
              }
            });
        },
        error: function (data) {
            var errmsg = "There was an error calling api: " + getAllTasksApi();
            console.log(errmsg);
            alert(errmsg);
        }
    });
}

$("#primary-blue-button").click(function(){
    // loadPrimaryPage();
    showModal();
})

$("#in-modal-new-task-button").click(function(){

    var newTaskData = getModalContent();

    if (!newTaskData) {
        // alert("No data");
        return;
    }

    console.log(newTaskData);

    $.ajax({
        type: 'POST',
        url: getNewTasksApi(),
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(newTaskData),
        success: function (data, textStatus, jQxhr) {
            var errmsg = `Successfully added new task: data: ${data}, textStatus: ${textStatus}, errorThrown: ${jQxhr}`;
            console.log(errmsg);
            // console.log("Loading primary page");
            // var source = $("#table-data-template").html();
            // var template = Handlebars.compile(source);
            // $('#primary-tasks-table-body').html(template({tasks: data}));
            // loadPrimaryPage();
            // $('.ui.calendar').calendar({
            //   type: 'date'
            // });
        },
        error: function (jqXhr, textStatus, errorThrown ) {
            var errmsg = `There was an error calling api: ${getNewTasksApi()}, textStatus: ${textStatus}, errorThrown: ${errorThrown}`;
            // var errmsg = "There was an error calling api: " + getNewTasksApi() + " --- " + JSON.stringify(data);
            console.log(errmsg);
            alert(errmsg);
        }
    });

    loadPrimaryPage();
})

function getModalContent(){
    var textAreaContent = $("#in-modal-task-detail-textarea").val();
    var dueDateContent = $("#in-modal-due-date").val();

    var data = {};
    if (!textAreaContent) {
        return null;
    }

    data['detail'] = textAreaContent;

    if (dueDateContent) {
        console.log(dueDateContent);
        // data['due_date'] = dueDateContent; //TODO: need to format this.
        var parts = dueDateContent.split("-")

        if (parts.length >= 3) {
            date_format = {
                year: parseInt(parts[0]),
                month: parseInt(parts[1]),
                day: parseInt(parts[2])
            }

            data['due_date'] = date_format;
        }

    }

    return data;
}

function getAllTasksApi() {
    return window.location.protocol + "//" + window.location.host + "/api/tasks";
}

function getNewTasksApi() {
    return window.location.protocol + "//" + window.location.host + "/api/new";
}

window.addEventListener("keydown", keyboardHandler, false);

function keyboardHandler(e) {

    if (event.defaultPrevented) {
        return; // Do nothing if the event was already processed
    }

    // console.log(event.key);

    switch (event.key) {

        case "N":
        case "n":
            showModal();
            // code for "down arrow" key press.
            // window.scrollBy(0, 500);

            break;

        // case "ArrowUp":
        //     // code for "up arrow" key press.
        //     window.scrollBy(0, -500);
        //     break;
        //
        // case "ArrowLeft":
        //     // code for "left arrow" key press.
        //     previousRuku();
        //     break;
        //
        // case "ArrowRight":
        //     // code for "right arrow" key press.
        //     nextRuku();
        //     break;

        default:
            return; // Quit when this doesn't handle the key event.
    }

    // Cancel the default action to avoid it being handled twice
    event.preventDefault();
}
