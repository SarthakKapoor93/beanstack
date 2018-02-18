// So this is working a bit better now. There will still be one longer load time at the beginnning.
// This behaviour means that it gets your location everytime you go onto the maps page. But I don't think you'll be
// a lot of time there to be honest so that's probably fine.

var map;
var userPosition;
var allBeanstackMarkers = [];
var nonBeanstackMarkers = [];
var selectedBeanstackMarkers = []

function initMap(){


    changeMapMessage("BeanStack cafes that sell " + selectedCoffee );

    if (userPosition){
        // If we already have the user position just continue
        next(userPosition);
    } else {
        // If we don't have the position already then we need to get it
       if (navigator.geolocation) {
       var x = navigator.geolocation.getCurrentPosition(function(position) {
            userPosition = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        next(userPosition);

        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
        } else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
        }
    }
}


function next(userPosition){

    //Create a map centred on the coordinates
    map = new google.maps.Map(document.getElementById('map'), {
        center: userPosition,
        zoom: 15
    });

    // Place the users position on the map as a marker
    var marker = new google.maps.Marker({
        map: map,
        position: userPosition
    });


    // As default the selected cafes should be shown.
    doAjax(coffeeKey, function(){

        // Remove any non bean stack cafes from the map
        for (i = 0; i < nonBeanstackMarkers.length; i++){
            nonBeanstackMarkers[i].setMap(null);
        }

        // remove any all beanstack cafes from the map
        for (i = 0; i < allBeanstackMarkers.length; i++){
            allBeanstackMarkers[i].setMap(null);
        }
    });
}

//This function will take care of the bound etc before displaying the data
function last(markers){

    //  Make new bounds object
    var bound = new google.maps.LatLngBounds();
    // Add the current user position to it
    bound.extend(new google.maps.LatLng(userPosition.lat, userPosition.lng));

    if (markers.length > 0){
        // Iterate over the markers and add them to the bounds
        for (i = 0; i < markers.length; i++){
            bound.extend(new google.maps.LatLng(markers[i].position.lat(), markers[i].position.lng()))
        }
        b = bound.getCenter();
        center = {lat: b.lat(), lng: b.lng()};
        map.fitBounds(bound);
        map.setCenter(center);
    } else {
        // If there are no additional markers to add, show all beanstack cafes
        changeMapMessage("Sorry, no BeanStack cafes have this coffee in stock. Showing: all BeanStack cafes");

        doAjax(null, function(){
            // Remove any non-beanstack markers that may be on the map
            for (i = 0; i < nonBeanstackMarkers.length; i++){
                nonBeanstackMarkers[i].setMap(null);
            }

            // Remove all selected cafes
            for (i = 0; i < selectedBeanstackMarkers.length; i++){
                selectedBeanstackMarkers[i].setMap(null);
            }
        });
    }
}

// The event listener for the all beanstack cafes button
$('#beanstack-cafes').click(function(){

    changeMapMessage("All BeanStack cafes");

    doAjax(null, function(){
        // Remove any non-beanstack markers that may be on the map
        for (i = 0; i < nonBeanstackMarkers.length; i++){
            nonBeanstackMarkers[i].setMap(null);
        }

        // Remove all selected cafes
        for (i = 0; i < selectedBeanstackMarkers.length; i++){
            selectedBeanstackMarkers[i].setMap(null);
        }
    });
});

// The event listener for the selected cafes button
$('#select-cafe').click(function(){

    changeMapMessage("BeanStack cafes that sell " + selectedCoffee );

    doAjax(coffeeKey, function(){

        // Remove any non bean stack cafes from the map
        for (i = 0; i < nonBeanstackMarkers.length; i++){
            nonBeanstackMarkers[i].setMap(null);
        }

        // remove any all beanstack cafes from the map
        for (i = 0; i < allBeanstackMarkers.length; i++){
            allBeanstackMarkers[i].setMap(null);
        }
    });
})

/*
    This function does the actual ajax call. If coffee is present, it will
    get the coffee shops for that coffee, otherwise it will just get all the
    beanstack coffee shops.
*/
function doAjax(coffee_id, myCallBack){
    var query;
    if (coffee_id){
        query = {coffee_id: coffee_id};
    } else {
        query = {};
    }
    $.get('get-cafes', query, function(data){
        var positions = JSON.parse(data);
        for (i = 0; i < positions.length; i++) {
            var marker = new google.maps.Marker({
                map: map,
                position: {lat: parseFloat(positions[i].lat), lng: parseFloat(positions[i].lng)}
            });

            if(coffee_id){
                selectedBeanstackMarkers.push(marker);
            } else {
                allBeanstackMarkers.push(marker);
            }
         }
         if(coffee_id){
            last(selectedBeanstackMarkers);
         } else {
            last(allBeanstackMarkers);
         }
         myCallBack();
    });
}


// Gets the other non-beanstack cafes from google
$('#other-cafes').click(function(event){

    changeMapMessage("Other cafes near you.");

    var service = new google.maps.places.PlacesService(map);
                service.nearbySearch({
                location: userPosition,
                radius: 2000,
                type: ['cafe']
            }, callback);
});

// This is the callback from the places library
function callback(results, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
        }
    }

    // Remove any beanstack markers that may be on the map
    for (i = 0; i < allBeanstackMarkers.length; i++){
        allBeanstackMarkers[i].setMap(null);
    }

    // Remove any selected markers that may be on the map
    for (i = 0; i < selectedBeanstackMarkers.length; i++){
        selectedBeanstackMarkers[i].setMap(null);
    }

    last(nonBeanstackMarkers);
}

function createMarker(place) {
    var placeLoc = place.geometry.location;
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
        }
    );
    nonBeanstackMarkers.push(marker);

google.maps.event.addListener(marker, 'click', function() {
  infowindow.setContent(place.name);
  infowindow.open(map, this);
});
}

function changeMapMessage(message){
    $('#map-message').html(message);
}