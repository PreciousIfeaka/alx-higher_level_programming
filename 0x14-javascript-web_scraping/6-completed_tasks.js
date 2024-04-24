const url = process.argv[2];
req = require('request');

req.get(`${url}`, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        let done = {};
        let item = JSON.parse(body);
        for (let i = 0; i < item.length; i++) {
            let key = item[i]["userId"];
            if (item[i]["completed"]) {
               if (done[key]) {
                done[key]++;
               }
               else {
                done[key] = 1;
               }
            }
        }
        console.log(done);
    }
})