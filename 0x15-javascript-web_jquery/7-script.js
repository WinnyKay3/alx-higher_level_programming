// use jquery to make an AJAX GET request to SWAPI URL
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
 // update the content of div id char element with char name
  $('#character').text(data.name);
});
