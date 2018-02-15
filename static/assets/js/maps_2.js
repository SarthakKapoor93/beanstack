

// So this is working a bit better now. There will still be one longer load time at the beginnning.
// This behaviour means that it gets your location everytime you go onto the maps page. But I don't think you'll be
// a lot of time there to be honest so that's probably fine.



var map;
var beanstackCafes = true;
var userPosition;
var beanstackMarkers = [];
var nonBeanstackMarkers = [];


function initMap(){


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

}

//This function will take care of the bound etc before displaying the data
function last(markers){

//  make new bounds object
    var bound = new google.maps.LatLngBounds();
    // add the current user position to it
    bound.extend(new google.maps.LatLng(userPosition.lat, userPosition.lng));

    //iterate over the markers and add them to the bounds
    for (i = 0; i < markers.length; i++){
        bound.extend(new google.maps.LatLng(markers[i].position.lat(), markers[i].position.lng()))
    }

    b = bound.getCenter();
    center = {lat: b.lat(), lng: b.lng()};
    map.fitBounds(bound);
    map.setCenter(center);
}


// Gets all beanstack cafes from the database and places their markers on the map
$('#beanstack-cafes, #select-cafe').click(function(event){

    // Remove any non beanstack markets that may be on the map
    for (i = 0; i < nonBeanstackMarkers.length; i++){
        nonBeanstackMarkers[i].setMap(null);
    }


    // get the coordinates for the cafes and put them on the map
    $.get('cafes', {}, function(data){
        var positions = JSON.parse(data);

        for (i = 0; i < positions.length; i++) {
            var marker = new google.maps.Marker({
                map: map,
                position: {lat: parseFloat(positions[i].lat), lng: parseFloat(positions[i].lng)}
            });
            beanstackMarkers.push(marker);
            marker.setMap(map);
         }
          last(beanstackMarkers);
    });
});


// Gets the other non-beanstack cafes from google
$('#other-cafes').click(function(event){
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
    for (i = 0; i < beanstackMarkers.length; i++){
        beanstackMarkers[i].setMap(null);
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



