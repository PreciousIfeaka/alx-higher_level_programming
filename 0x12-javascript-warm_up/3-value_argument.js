#!/usr/bin/node
const clArguments = process.argv;
if (clArguments[2] == null) {
  console.log('No argument');
} else {
  console.log(clArguments[2]);
}
