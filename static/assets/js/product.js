$(function(){
    $('#modal-message').hide();
});

$('#review-button').click(function(event){
    document.getElementById('review-heading').scrollIntoView({behavior: "smooth"});
});

$('#vendor-button').click(function(event){
    document.getElementById('vendor-heading').scrollIntoView({behavior: "smooth"});
});


$('#add-button').click(function(){
    $('#my-modal').modal('toggle');
});

// This is the event listener for the accordian effect in the add to beanstack modal
$('#modal-add, #arrow-glyph').click(function(){
    $('.collapse').collapse('hide');
    $('#class-to-add').addClass('panel-default').removeClass('panel-primary');
    $('#class-to-add').css("margin-bottom", "5px");
    $('#modal-message').show();
    $('#spacer').hide();
});

// Make the arrow and the add button both react when one is hovered over
$('#arrow-glyph, #modal-add').hover(function(){
    $('#arrow-glyph').css('color', '#3174AE');
    $('#modal-add').addClass('btn-primary');
}, function(){
    $('#arrow-glyph').css('color', '#DDDDDD');
    $('#modal-add').removeClass('btn-primary');
});



