$(function(){
    $('#modal-message').hide();
});

// Resizes the window took this from stack overflow
$(window).bind('resize', function(e)
{
  if (window.RT) clearTimeout(window.RT);
  window.RT = setTimeout(function()
  {
    this.location.reload(false);
  }, 100);
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


// This is called from the maps.js script
function activate_modal(marker){
    $('#vendor-detail-modal .modal-title').html(marker.name);
    $('#vendor-detail-modal .modal-body #description').html(marker.description);
    $('#vendor-detail-modal .modal-body #online-shop').html("<a href=" + marker.onlineshop + " >visit online shop</a>");
    $('#vendor-detail-modal .modal-body #address').html(marker.address);
    $('#vendor-detail-modal .modal-body #products').html("");
    for (i = 0; i < marker.products.length; i++){
        $('#vendor-detail-modal .modal-body #products').append("<li>"+ marker.products[i] + "</li>");
    }
    $('#vendor-detail-modal').modal('toggle');
}
