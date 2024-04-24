#!/usr/bin/node
const request = require('request');
let count = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const conbody = JSON.parse(body);
    conbody.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(18)) {
          count = count + 1;
        }
      });
    });
    console.log(count);
  }
});
