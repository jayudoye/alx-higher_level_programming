#!/usr/bin/node

const request = require ('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information. Status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
