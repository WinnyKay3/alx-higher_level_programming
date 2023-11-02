// use jquery to make AJAX GET request to the sqapi url
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  // get the array of movies from response data
  const movies = data.results;

  // iterate thru movies and append each title to the <ul id= "list_movies">
  for (const movie of movies) {
     const title = movie.title;
     $('#list_movies').append(`<li>${title}</li>`);
   }
});
