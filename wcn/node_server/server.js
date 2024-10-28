const http = require('http');


const hostname = '127.0.0.1'; 
const port = 3000;


const server = http.createServer((req, res) => {
    res.statusCode = 200; 
    res.setHeader('Content-Type', 'text/html'); 
    res.end('<h1>My Name: Rutuparna Kolte</h1><h2>PRN: 122A9042</h2>'); 
});

// Start the server
// node server.js
// go to localhost

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}`);
})