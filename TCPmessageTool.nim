import net
import std/parseopt

var p = initOptParser("-ab -e:5 --foo --bar=20 file.txt")

let server: Socket = newSocket()
server.bindAddr(Port(5555))

stdout.writeLine("Server: started. Listening to new connections on port 5555 ... ")
server.listen()

let client: Socket = newSocket()
client.connect("127.0.0.1", Port(5555))
stdout.writeLine("Client: connected to server on address 127.0.0.1:5555")

client.close()


server.close()
stdout.writeLine("Server: closed.")
