#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersNames = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, __, charactersBody) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(charactersBody).name);
        });
      }));

    Promise.all(charactersNames)
      .then(characterNames => console.log(characterNames.join('\n')))
      .catch(errors => console.log(errors));
  });
}
