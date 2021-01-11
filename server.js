// var net = require('net');
// var server = net.createServer(function (connection) {
//     console.log('client connected');
//     connection.on('end', function () {
//         console.log('客户端关闭连接');
//     });
//     connection.write('Hello World!\r\n');
//     connection.pipe(connection);
// });
// server.listen(8080, function () {
//     console.log('server is listening');
// });

var net = require('net')

function user(uname, host, port) {
    this.uname = uname
    this.host = host
    this.port = port
}

var port_ind = 8889

users = new Map()
addrs = new Map()

var transmit = async function (address, message) {
    connection = net.connect({host:address.address, port = address.port})
}

var add_user = function (address) {
}

var server = net.createServer(function (connection) {
    let address = connection.address()
    if (!addrs.has(address)) {
        connection.on('data', (uname) => {
            
        })
    }
})


server.listen(8888, '127.0.0.1', () => {
    console.log('server is lisitening')
})

server.on('connection', (connection) => {
    console.log('new connection: ', connection)
})

server.on('error', (error) => {
    console.error(error)
})
