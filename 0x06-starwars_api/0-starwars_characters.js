#!/usr/bin/node
/**
 * Script to fetch and display the names of characters in a Star Wars film.
 *
 * Usage:
 * - The script accepts a single argument, which is the ID of a Star Wars film.
 * - It fetches the film details from the Star Wars API (SWAPI).
 * - It retrieves and prints the names of all characters appearing in the specified film.
 */

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if a film ID argument is provided
if (process.argv.length > 2) {
  // Make a request to the Star Wars API to get film details using the provided ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }

    // Extract the URLs of the characters appearing in the film
    const charactersURL = JSON.parse(body).characters;

    // Map each character URL to a promise that fetches the character's name
    const charactersName = charactersURL.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
            return;
          }
          // Resolve the promise with the character's name
          resolve(JSON.parse(charactersReqBody).name);
        });
      });
    });

    // Once all character names are fetched, print them line by line
    Promise.all(charactersName)
      .then((names) => {
        console.log(names.join('\n'));
      })
      .catch((allErr) => {
        console.error(allErr);
      });
  });
}
