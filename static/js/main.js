function initAutocomplete(inputId, mapId) {
  var map = new google.maps.Map(document.getElementById(mapId), {
    center: {
      lat: 48,
      lng: 4
    },
    zoom: 4,
    disableDefaultUI: true
  });

  // Create the search box and link it to the UI element.
  var input = document.getElementById(inputId);
  var autocomplete = new google.maps.places.Autocomplete(input);
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);
  var marker = new google.maps.Marker({
    map: map
  });

  // Bias the SearchBox results towards current map's viewport.
  autocomplete.bindTo('bounds', map);
  // Set the data fields to return when the user selects a place.
  autocomplete.setFields(
    ['address_components', 'geometry', 'name']);
  
  //Below condition is to change the marker in maps as per selection 
  /*
  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  autocomplete.addListener('place_changed', function() {
    var place = autocomplete.getPlace();
    if (!place.geometry) {
      console.log("Returned place contains no geometry");
      return;
    }
    var bounds = new google.maps.LatLngBounds();
    marker.setPosition(place.geometry.location);

    if (place.geometry.viewport) {
      // Only geocodes have viewport.
      bounds.union(place.geometry.viewport);
    } else {
      bounds.extend(place.geometry.location);
    }
    map.fitBounds(bounds);
  });
  */
}

document.addEventListener("DOMContentLoaded", function(event) {
  initAutocomplete('my-input-searchbox', 'map');
});

$(document).ready(function(){
  $("#transportBtn").click(function(){
    $("#myModal").modal();
    initAutocomplete('my-input-searchbox-departure', 'map-departure');
    initAutocomplete('my-input-searchbox-arrival', 'map-arrival');
  });
  $("#shiftingBtn").click(function(){
    $("#myModal2").modal();
    initAutocomplete('my-input-searchbox-departure2', 'map-departure2');
    initAutocomplete('my-input-searchbox-arrival2', 'map-arrival2');
  });
  $("#togBtn").click(function(){
   $(this).next().toggleClass("after");
  })
});
