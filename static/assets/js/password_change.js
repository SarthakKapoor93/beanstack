// Because we are using Django redux to do password resetting, we don't have access
// to the view that handles this. Instead we make an ajax call to retrieve the data
// that we need.
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