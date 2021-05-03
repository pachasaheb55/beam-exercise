
var url = 'http://localhost:8000/';
var locations = '';
var lat = '';
var long = '';
var distance = '';
var measurement = '';

$( document ).ready(function() {
  retrieveScooters()  
});

function myMap() {
  if(lat == '' && long == ''){
    var mapProp= {
      center:new google.maps.LatLng(1.361362, 103.820890),
      zoom:11,
    };}
    else{
      var mapProp= {
        center:new google.maps.LatLng(lat, long),
        zoom:15,
      };
    }
    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
    for(loc of locations){
    new google.maps.Marker({
      position: new google.maps.LatLng(loc.latitude, loc.longitude),
      map,
      icon: url+'static/img/scooter.png/',
      title: String(loc.scooters)
    });  
    }
    if(measurement == 'km'){
      distance = distance*1000
    }
    if(measurement == 'mile'){
      distance = distance*1609.34
    }
    if(lat != '' && long !='') {
      // Add the circle for this city to the map.
       new google.maps.Circle({
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35,
        map,
        center: new google.maps.LatLng(lat, long),
        radius: distance-200,
      });
      new google.maps.Marker({
        position: new google.maps.LatLng(lat, long),
        map,
        icon: url+'static/img/walking.png/',
        title: 'User Location'
      });  
    }
  }

function saveScooters(){
    request = {
        'lat': $("#lat").val(),
        'long': $("#long").val(),
        'scooters': $("#scooters").val()
    }
    $.post(url+"beam/saveScooters/", JSON.stringify(request), function(result){
      },"json");
}

function retrieveScooters(){
    $.get(url+"beam/retrieveScooters/", function(data, status){
        if(status == "success"){
            locations = data;
            myMap()
            initializeTable(data);
        }
      });
}

  function searchScooters(){
    lat= $("#lat-search").val()
    long= $("#long-search").val()
    distance= parseInt($("#distance").val())
    measurement= $("#measurement").val()
  $.get(url+"beam/searchScooters/"+lat+"/"+long+"/"+distance+"/"+measurement+"/", function(data, status){
    if(status == "success"){
    myMap()
    $('#Locations_Table').DataTable().destroy();
    initializeTable(data.result);
    }
  });
  }

function initializeTable(data){
  $('#Locations_Table').DataTable({
    data: data,
    columns: [
      { 'data': 'id' },
      { 'data': 'latitude' },
      { 'data': 'longitude' },
      { 'data': 'scooters' },
    ]});
}