#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information. Status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    const wedgeAntillesMovies = movieData.results.filter(movie => movie.characters.some(character => character.endsWith(`/${characterId}/`)));

    console.log(wedgeAntillesMovies.length);
  }
});
