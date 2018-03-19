
var map;
var userPosition;
var allBeanstackMarkers = [];
var nonBeanstackMarkers = [];
var selectedBeanstackMarkers = []
var vendor_data = []

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

    // Place the user's position on the map. User the standard red marker
    // if on mobile devive otherwise use the custom blue one.
    if (!('ontouchstart' in document)){
        var marker = new google.maps.Marker({
            icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
            map: map,
            position: userPosition
        });
    } else {
        var marker = new google.maps.Marker({
            map: map,
            position: userPosition
        });
    }

    // Create an info window for the user
    var infowindow = new google.maps.InfoWindow({
        content: "<b>You are here</b>",
        });

    // Action listener on the users marker
    marker.addListener('mouseover', function(){
        infowindow.open(map, marker);
    });

    // Make sure the infowindow closes again when the mouse rolls out
    marker.addListener('mouseout', function() {
        infowindow.close();
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

        // Put the data on the vendors into a global dict of vendors
        vendor_data = positions;

        for (i = 0; i < positions.length; i++) {
            var marker = new google.maps.Marker({
                map: map,
                position: {lat: parseFloat(positions[i].lat), lng: parseFloat(positions[i].lng)},
                name: vendor_data[i]['business_name'],
                description: vendor_data[i]['description'],
                onlineshop: vendor_data[i]['online-shop'],
                address: vendor_data[i]['address'],
                products: vendor_data[i]['products']
            });

            // Create an info window for each of the beanstack cafes
            var infowindow = new google.maps.InfoWindow();

            // Put action listeners on each of the markers and set the text to be displayed
            google.maps.event.addListener(marker, 'mouseover', function(){
                var content = "<b>" + this.name + "</b><br> <small>click marker for info</small>"
                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            // Make sure the infowindow closes again when the mouse rolls out
            google.maps.event.addListener(marker, 'mouseout', function() {
                infowindow.close();
            });

            // Create an event listener for each of the markers
            google.maps.event.addListener(marker, 'click', function() {
                activate_modal(this);
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

    // Create an info window for the marker diplaying the name of the cafe
    var infowindow = new google.maps.InfoWindow({
        content: "<b>" + place.name + "</b>",
        });

    // Function for click or rollover
    clickRollover = function(){
        infowindow.open(map, marker);
    };

    // Action listener on the marker
    marker.addListener('mouseover',  clickRollover);

    // Additional click listener for touch screen devices
    marker.addListener('click',  clickRollover);

    // Make sure the infowindow closes again when the mouse rolls out
    marker.addListener('mouseout', function() {
        infowindow.close();
    });

    nonBeanstackMarkers.push(marker);
}

function changeMapMessage(message){
    $('#map-message').html(message);
}