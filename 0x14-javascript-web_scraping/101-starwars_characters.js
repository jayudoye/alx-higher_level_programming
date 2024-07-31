#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./swMovieCharacters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information. Status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    const characters = [];
    let charactersFetched = 0;

    characterUrls.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          characterData.id = characterUrl.split('/')[5];
          characters.push(characterData);

          charactersFetched++;
          if (charactersFetched === characterUrls.length) {
            characters.sort((a, b) => a.id - b.id);

            characters.forEach(character => {
              console.log(character.name);
            });
          }
        } else {
          console.error('Error retrieving character information. URL:', characterUrl);
        }
      });
    });
  }
});
