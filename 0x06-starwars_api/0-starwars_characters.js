#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  async function (err, res, body) {
    if (err) return console.error(err);
    const urlList = JSON.parse(body).characters;
    for (const url of urlList) {
      await new Promise(function (resolve, reject) {
        request(url, function (err, res, body) {
          if (err) return console.error(err);
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  });
