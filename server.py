from xmlrpc.server import SimpleXMLRPCServer
import os


server = SimpleXMLRPCServer(('localhost', 9999))

def receive_file(arg):
    with open("./tmp/out.jpg", 'wb') as handle:
        handle.write(arg.data)
        return True

server.register_function(receive_file, 'receive_file')
print("running")
server.serve_forever()