#!/usr/bin/node
const ps = require('process');
const nOcc = parseInt(process.argv[2]);
if (isNaN(nOcc)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nOcc; i++) {
    console.log('C is fun');
  }
}
