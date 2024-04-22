const fs = require('fs');
const process = require('process');
const file = process.argv[2];
fs.readFile(`${file}`, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
