#!/usr/bin/node
const argv = process.argv;
if (parseInt(argv[2])) {
  for (let count = 0; count < parseInt(argv[2]); count++) {
    console.log('X'.repeat(parseInt(argv[2])));
  }
} else console.log('Missing size');
