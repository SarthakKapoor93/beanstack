

function getPosition(){
    console.log("javascript working")
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(function(position){

            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            $.get('/bean_app/get_nearby/', {'lat': pos.lat, 'long': pos.lng}, function(data){
                // Once the AJAX call has been made
                map = $('#map')
                var marker = new google.maps.Marker({
                    position: data,
                    map: map
                    });
        })
    } else {
        console.log('geolocation failed for some reason.')
    }
}

}
      // This example requires the Places library. Include the libraries=places
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

      var map;
      var infowindow;

      function initMap() {
        var pyrmont = {lat: -33.867, lng: 151.195};



         if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };


            map = new google.maps.Map(document.getElementById('map'), {
                    center: pyrmont,
                    zoom: 15
              });

            infowindow = new google.maps.InfoWindow();
            var service = new google.maps.places.PlacesService(map);
            service.nearbySearch({
                location: pyrmont,
                radius: 500,
                type: ['store']
            }, callback);



            infoWindow.setPosition(pos);
            infoWindow.setContent('You are here.');
            map.setCenter(pos);
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
        });

        google.maps.event.addListener(marker, 'click', function() {
          infowindow.setContent(place.name);
          infowindow.open(map, this);
        });
      }