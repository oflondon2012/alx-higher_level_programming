// script that fetches the character name from the given url
let apiurl = 'https://swapi.co/api/people/5/?format=json';
$.get(apiurl, function (data, stat) {
  $('div#character').text(data.name);
});
