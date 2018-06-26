

var map, infoWindow;
function initMap() {
map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: -34.397, lng: 150.644},
  zoom: 18
});
// Try HTML5 geolocation.

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
    var pos = {
      lat: position.coords.latitude,
      lng: position.coords.longitude
    };
    console.log(pos)

    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: 'My location!'
    });
    var latlngbounds = new google.maps.LatLngBounds();
    map.setCenter(pos);
    $.get( "/foursquare/places/", { lat: pos.lat, lng: pos.lng } )
          .done(function( data ) {
            dataset = []
            $.each( data.data.venues, function() {
                var markerImage = {
                    url: 'https://image.flaticon.com/icons/svg/33/33622.svg',
                    scaledSize: new google.maps.Size(24, 24),
                    origin: new google.maps.Point(0,0),
                    labelOrigin: new google.maps.Point(5, 30)
                },
                markerOptions = {
                    map: map,
                    position: new google.maps.LatLng(this.venue.location.lat, this.venue.location.lng),
                    icon: markerImage,
                    label: this.venue.name,
                    url:"/buy?venue=" + this.venue.id,
                    },
                marker = new google.maps.Marker(markerOptions);
                latlngbounds.extend(marker.position);
                if (typeof this.venue.location.address == 'undefined'){
                    address = "";
                }
                else{
                address = this.venue.location.address;
                }
                dataset.push([this.venue.name, address, 0.0])
                google.maps.event.addListener(marker, 'click', function() {
                    window.location.href = this.url;
                });
            });

            //Center map and adjust Zoom based on the position of all markers.
            map.setCenter(latlngbounds.getCenter());
            map.fitBounds(latlngbounds);
            $('#placesData').DataTable( {
                data: dataset,
                searching:false,
                paging:false,
                info:false,
                columns: [
                    { title: "Name" },
                    { title: "Address" },
                    { title: "Price" },
                ]
            } );

          });

    google.maps.event.addListenerOnce(map, 'bounds_changed', function(event) {
          this.setZoom(map.getZoom()-1);

          if (this.getZoom() > 15) {
            this.setZoom(15);
          }
        });

  }, function() {
    handleLocationError(true, infoWindow, map.getCenter());
  });
} else {
  // Browser doesn't support Geolocation
  handleLocationError(false, infoWindow, map.getCenter());
}

}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
alert("Geo location not supported, Please enable geolocation settings in browser");
}


function buyMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: lat, lng: long},
      zoom: 18
    });
    var pos = {
      lat: lat,
      lng: long
    };
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: name,
    });
}


