// 192.168.1.104

const http = require('http')

const hostname = '192.168.1.104'
const port = '8000'

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html')
    res.end('<h1>Hello, Safari!</h1>');
});

server.listen(port, hostname, () => {
    console.log('Server running at http://${hostname}:${port}/');
});