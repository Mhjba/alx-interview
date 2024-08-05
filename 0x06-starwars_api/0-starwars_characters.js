#!/usr/bin/node

const req = require('request');
const util = require('util');

// Get the film ID
const film_Id = process.argv[2];

// Construct the URL
const URL = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// Promisify the request function
const prequest = util.promisify(req);

(async () => {
  try {
    // Fetch the film details
    const film = (await prequest(URL, { json: true })).body;

    // Iterate over the list of character URLs
    for (const url of film.characters) {
      // Fetch each character's details
      const char = (await prequest(url, { json: true })).body;
      // Print the character's name
      console.log(char.name);
    }
  } catch (error) {
    // Handle error
    console.log(error);
  }
})();
