function openInNewTab(url) {
    var win = window.open(url, '_blank');
    win.focus();
}

function showModal() {
    $('.ui.modal').modal('show');
}


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
            $('#primary-tasks-table-body').html(template({tasks: data}));

        },
        error: function (data) {
            var errmsg = "There was an error calling api: " + getAllTasksApi();
            console.log(errmsg);
            alert(errmsg);
        }
    });
}

$("#primary-blue-button").click(function(){
    loadPrimaryPage();
})

function getAllTasksApi() {
    return window.location.protocol + "//" + window.location.host + "/api/tasks";
}
