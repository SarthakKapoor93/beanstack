// This example requires the Places library. Include the libraries=places
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

// There are three functions that I need from this js.
//    - create a map with a user and other coffee shops
//    - create a map with the user and one beanstack coffee shop
//    - create a map with all beanstack coffee shops and the user

var map;
var infowindow;


function initMap() {


    // Get the coordinates of the user
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };

        var center = pos;

        // Create a map centred on the coordinates
        map = new google.maps.Map(document.getElementById('map'), {
            center: pos,
            zoom: 15
        });

        // Place the users position on the map as a marker
        var marker = new google.maps.Marker({
            map: map,
            position: pos
        });

        // If a single beanstack coffee shop or all beanstack coffees shops have been selected, show markers
        if (beanstackCafes || selectedCafe){

            var bound = new google.maps.LatLngBounds();
            bound.extend(new google.maps.LatLng(pos.lat, pos.lng));

            for (i = 0; i < positions.length; i++) {
                var marker = new google.maps.Marker({
                    map: map,
                    position: {lat: parseFloat(positions[i].lat), lng: parseFloat(positions[i].lng)}
                });

                bound.extend(new google.maps.LatLng({lat: parseFloat(positions[i].lat), lng: parseFloat(positions[i].lng)}));
             }

            b = bound.getCenter();
            center = {lat: b.lat(), lng: b.lng()};
            map.fitBounds(bound);

        }


        // Search for cafes near the position
        var infowindow = new google.maps.InfoWindow();

        // Show other cafes according to the boolean flag
        if (otherCafes){
             var service = new google.maps.places.PlacesService(map);
                service.nearbySearch({
                location: pos,
                radius: 2000,
                type: ['cafe']
            }, callback);
        }


      infoWindow.setPosition(pos);
      infoWindow.setContent('You are here.');
      map.setCenter(center);
      }, function() {
        handleLocationError(true, infoWindow, map.getCenter());
      });
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
}

function callback(results, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
        }
    }
}

function createMarker(place) {
    var placeLoc = place.geometry.location;
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
        }
    );

google.maps.event.addListener(marker, 'click', function() {
  infowindow.setContent(place.name);
  infowindow.open(map, this);
});
}

$(window).ready(function() {
    $('#loading').hide();
});



