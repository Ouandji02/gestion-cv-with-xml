const http = require('http')
const app = require('./App')


http.createServer(app).listen(5000)