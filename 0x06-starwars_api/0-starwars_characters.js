#!/usr/bin/node
const id = process.argv.slice(2);
const url = `https://swapi-api.hbtn.io/api/films/${id[0]}/`;

const request = require('request');
request(url, async function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const bodyJson = JSON.parse(body);
  for (const characters of bodyJson.characters) {
    await new Promise(function (resolve, reject) {
      request(characters, function (error, response, body) {
        if (error) {
          return console.error(error);
        }
        const bdJson = JSON.parse(body);
        console.log(bdJson.name);
        resolve();
      });
    });
  }
});
