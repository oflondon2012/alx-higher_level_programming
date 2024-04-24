#!/usr/bin/node
// Star Wars

const request = require('request');
const baseurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(baseurl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
