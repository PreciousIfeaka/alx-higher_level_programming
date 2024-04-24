#!/usr/bin/node
const proc = process.argv[2]; // The second argument is the movie number
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${proc}`;

request.get(`${url}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const character = JSON.parse(body).characters; // parsing the body to an object type is necessary
    for (let i = 0; i < character.length; i++) { // loops through the characters' url
      const url1 = character[i];
      request.get(`${url1}`, (error, response, body) => { // request each character url
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body).name;
          console.log(names); // print out the name;
        }
      });
    }
  }
});
