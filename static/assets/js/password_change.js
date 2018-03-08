// We need to do an ajax call to the server to get the saved coffees to display on this page
$(function(){

    $.get('/bean_app/get-saved-coffees', {}, function(data){
        var data = JSON.parse(data);
        var selector = $('#selecter')
        // loop over the data and insert into the html list
        for (i = 0; i < data.length; i++) {
            var name = data[i].name;
            selector.append("<option style='color: #999999;' value=''>" + name + "</option>");
        }
    });

});