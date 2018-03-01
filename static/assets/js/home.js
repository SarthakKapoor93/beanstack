$('#arrowbutton').click(function(event){
    document.getElementById('heading').scrollIntoView({behavior: "smooth"});
});

$('#arrowbutton').hover(function(event){
    var $button = $('#arrowbutton')
    $button.css("opacity", "0.6");
}, function(event){
    $('#arrowbutton').css("opacity", "0.2");
});