var net = require('net')

var port_ind = 8889

var users = new Map()       // key: uname & value: address

var transmit = async function (uname, message) {
    for (let user of users.entries()) {
        if (user[0] == uname) continue
        let connection = net.connect(user[1])
        connection.on('error', (err) => {
            users.delete(user[0])
            console.log(user[0] + 'lost connection');
        })
        await connection.write(uname + ': ' + message)
        connection.end()
    }
}

var server = net.createServer(function (connection) {
    connection.on('data', (data) => {
        let pattern = /~(.+)~#~(.+)~#~(.*)~/    // ~(command)~#~(uname)~#~(text)~
        let groups = pattern.exec(data)
        if (groups !== null) {
            if (groups[1] == 'login') {
                if (!users.has(groups[2])) {
                    connection.write('ok' + port_ind)
                    users.set(groups[2], { port: port_ind, host: '127.0.0.1' })
                    port_ind += 1
                    console.log('add user: ' + groups[2]);
                }
                else {
                    connection.write('uname if exist')
                }
            }
            else if (groups[1] == 'msg') {
                transmit(groups[2], groups[3]).then(() => console.log('transmit: ' + groups[2] + '# ' + groups[3]))
                // console.log('transmit: ' + groups[2] + '#' + groups[3])
            }
            else {
                console.error('invalid command: ' + data)
            }
        }
        else {
            console.error('format error: ' + data)
        }
        connection.end()
    })

})


server.listen(8888, '127.0.0.1', () => {
    console.log('server is lisitening')
})

server.on('connection', (connection) => {
    console.log('new connection: ', connection.address())
})

server.on('error', (error) => {
    console.error(error)
})

