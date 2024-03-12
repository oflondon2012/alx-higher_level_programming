#!/usr/bin/node
const argv = process.argv;
if (parseInt(argv[2])) {
  for (let count = 0; count < parseInt(argv[2]); count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
