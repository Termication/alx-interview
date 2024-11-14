#!/usr/bin/node

/**
 * Script to print all character names of a given Star Wars movie.
 * The first argument passed is the Movie ID (e.g., 3 = "Return of the Jedi").
 * Fetches and prints character names in the same order as listed in the "characters" array.
 * Uses the Star Wars API.
 */

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

/**
 * Recursive function to fetch and print character names one by one.
 * @param {string[]} characterList - List of character URLs.
 * @param {number} index - Current index in the character list.
 */
function sendRequest (characterList, index) {
  // Base case: if all characters have been processed, return.
  if (characterList.length === index) {
    return;
  }

  // Send a request to fetch the character details.
  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Parse the character name and print it.
      console.log(JSON.parse(body).name);

      // Recursively fetch the next character.
      sendRequest(characterList, index + 1);
    }
  });
}

/**
 * Fetch movie details using the given Movie ID.
 */
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Extract the list of character URLs from the movie response.
    const characterList = JSON.parse(body).characters;

    // Start fetching character names from the list.
    sendRequest(characterList, 0);
  }
});
