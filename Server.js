// Import dependencies
const express = require ('express');
const sqlite3 =
require( 'sqlite3').verbose ();
const bodyParser = require('body-
parser');
const path = require ('path');
// Initialize the app
const app = express ();
app. use (bodyParser.urlencoded < ex-
tended: false }));
// Create SQLite database (or open if
it exists)
const db = new
sqlite3. Database ('users.db');
// Create a table to store users if
it doesn't already exist
db. serialize (() => {
db. run ('CREATE TABLE IF NOT
EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email
TEXT) ' ) ;
}) ;
// Serve the HTML form
app. get('/', (req, res) =>
res. sendFile(path.join/__dirname,
'index.html')) ;
}) ;
// Handle form submission
app.post('/submit', (req, res) =>
｛
const { name, email } = req. body;
// Insert user data into the
database
db. run (' INSERT INTO users (name, email) VALUES (?, ?)', [name, emaill, (err) =>
{
if
(err) {
return
console.error (err.message);
｝
res. send('Data has been saved
to the database!');
}) ;
}) ;
// Start the server on port 3000
const PORT = 3000;
app. listen (PORT, () => {
console. log ( Server is running on http://localhost:${PORT}');
}) ;
