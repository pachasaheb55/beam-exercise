//Global variable declaration
var url = 'http://localhost:8000/';
var locations, lat, long, distance, measurement;
var singaporeLatLng = { lat: 1.361362, lng: 103.820890, center: 15 };

//Function to execute on page load
$(document).ready(function () {
  //Function to retrive available scooters
  retrieveScooters()
});

//Function to load map
function myMap() {
  // created a map property for centering and zoom of map
  var mapProp = {
    center: '',
    zoom: '',
  };
  // if condition to check for user search lat and long
  if (lat == '' && long == '') {
    // Assigning Singaport Location as center for map
    mapProp.center = new google.maps.LatLng(singaporeLatLng.lat, singaporeLatLng.lng);
    mapProp.zoom = singaporeLatLng.center
  }
  else {
    // Assigning user location as center of the map
    mapProp.center = new google.maps.LatLng(lat, long);
    mapProp.zoom = 15
  }
  // initialize a map 
  var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
  // for loop for marking the scooters on map
  for (loc of locations) {
    //marker on google map
    new google.maps.Marker({
      position: new google.maps.LatLng(loc.latitude, loc.longitude),
      map,
      icon: url + 'static/img/scooter.png/',
      // displays to total number of scooters available at a location
      title: String(loc.scooters)
    });
  }
  // checking for distance and converting into meters
  if (measurement == 'km') {
    distance = distance * 1000
  }
  if (measurement == 'mile') {
    distance = distance * 1609.34
  }
  // creating a circle shape on map according to radius given
  if (lat != '' && long != '') {
    // Add the circle for this city to the map.
    new google.maps.Circle({
      strokeColor: "#FF0000",
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: "#FF0000",
      fillOpacity: 0.35,
      map,
      center: new google.maps.LatLng(lat, long),
      radius: distance - 200,
    });
    // adding marker for the user lat and long
    new google.maps.Marker({
      position: new google.maps.LatLng(lat, long),
      map,
      icon: url + 'static/img/walking.png/',
      title: 'User Location'
    });
  }
}

//Function to save data of scooters
function saveScooters() {
  // getting the values from html based on ids
  request = {
    'lat': $("#lat").val(),
    'long': $("#long").val(),
    'scooters': $("#scooters").val()
  }
  // Jquery POST call to backend api for saving data of scooters
  $.post(url + "beam/saveScooters/", JSON.stringify(request), function (result) {
  }, "json");
}


//Function to retrieve the scooters from the backend api
function retrieveScooters() {
  // Jquery GET call to retrieve scooters data
  $.get(url + "beam/retrieveScooters/", function (data, status) {
    // if status is success initialize map and datatable functions
    if (status == "success") {
      locations = data;
      myMap()
      initializeTable(data);
    }
  });
}

// Function to search scooters at given lat, long and radius(distance)
function searchScooters() {
  // Get the HTML field Values using Jquery
  lat = $("#lat-search").val()
  long = $("#long-search").val()
  distance = parseInt($("#distance").val())
  measurement = $("#measurement").val()
  get_url = lat + "/" + long + "/" + distance + "/" + measurement + "/"
  // JQuery GET call for the available scooters nearby
  $.get(url + "beam/searchScooters/" + get_url, function (data, status) {
    // if status is success initialize map and datatable functions
    if (status == "success") {
      myMap()
      $('#Locations_Table').DataTable().destroy();
      initializeTable(data.result);
    }
  });
}

// Intialize Jquery datatable for displaying the list of locations
function initializeTable(data) {
  $('#Locations_Table').DataTable({
    data: data,
    columns: [
      { 'data': 'id' },
      { 'data': 'latitude' },
      { 'data': 'longitude' },
      { 'data': 'scooters' },
    ]
  });
}