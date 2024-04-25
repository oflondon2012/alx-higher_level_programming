#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const jobs = JSON.parse(body);
    for (const i in jobs) {
      const job = jobs[i];
      if (job.completed === true) {
        if (completed[job.userId] === undefined) {
          completed[job.userId] = 1;
        } else {
          completed[job.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
