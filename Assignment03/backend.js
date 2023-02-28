
// Note to students: there's nothing you have to do here, other than run it...
// Instructions:
// ----------------
// CTRL+SHIFT+` to open Terminal,  then
// cd .\Assignment03
// npm install
// node backend.js

const express = require('express');
const app = express();
const cors = require('cors');
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(cors());

//"Database" of pledges
var pledges =[ 
    { "first_name":"Barney", "last_name": "Rubble", "email":"barney@bedrock.ca", "amount":"500", "datetime" : "2022-2-23"},
    { "first_name":"Betty", "last_name":"Rubble", "email":"betty@bedrock.ca", "amount":"600", "datetime" : "2022-2-23"},
    { "first_name":"Fred", "last_name":"Flintstone", "email":"Barney@bedrock.ca", "amount":"150", "datetime" : "2022-2-23"},
    { "first_name":"Wilma", "last_name":"Flintstone","email":"fred@bedrock.ca", "amount":"700", "datetime" : "2022-2-23"}
];

//retrieve the list of pledges (the client is making a GET request via AJAX to this server-side endpoint when report.html is loaded)
app.get('/api/pledges', (req, res) => {
    console.log("GET",req.params);

    //send all data back
    res.json(pledges);
})

//add a new pledge (the client is making the POST request via AJAX to this server-side endpoint, from page pledge.html)
app.post('/api/pledges', (req, res) => {
    console.log("POST",req.body);

    //add the new record to the array
    pledges.push(req.body);

    //response is usually the added record
    res.send(req.body);
})

app.listen(5000, () => {
    console.log('Listening on localhost:5000, try hitting the GET request at http://localhost:5000/api/pledges');
});

