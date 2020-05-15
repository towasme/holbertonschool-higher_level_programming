// script that fetches and lists all movies title
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let title of data.results) {
    $('UL#list_movies').append($('<li></li>').text(title.title));
  }
});
