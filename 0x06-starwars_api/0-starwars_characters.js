#!/usr/bin/node
/**
 * Script to print all characters of a given Star Wars movie.
 *
 * Usage:
 * - The first positional argument is the Movie ID (e.g., 3 = "Return of the Jedi").
 * - Fetches character names in the same order as listed in the "characters" array from the /films/ endpoint.
 */

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if a Movie ID is provided
if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const url = `${API_URL}/films/${movieId}/`;

  // Fetch the film details using the Movie ID
  request(url, (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }

    // Check for valid response status
    if (res.statusCode !== 200) {
      console.error(`Failed to fetch film. Status code: ${res.statusCode}`);
      return;
    }

    let charactersURL;
    try {
      charactersURL = JSON.parse(body).characters;
    } catch (parseErr) {
      console.error('Failed to parse JSON response:', parseErr);
      return;
    }

    // Function to fetch character names and display them in order
    const fetchCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (charErr, charRes, charBody) => {
          if (charErr) {
            reject(charErr);
          } else if (charRes.statusCode !== 200) {
            reject(new Error(`Failed to fetch character. Status code: ${charRes.statusCode}`));
          } else {
            try {
              const name = JSON.parse(charBody).name;
              resolve(name);
            } catch (nameParseErr) {
              reject(nameParseErr);
            }
          }
        });
      });
    };

    // Create a list of promises to fetch all character names
    const charactersPromises = charactersURL.map(fetchCharacterName);

    // Resolve all promises and print the character names in order
    Promise.all(charactersPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((allErr) => {
        console.error(allErr);
      });
  });
}
