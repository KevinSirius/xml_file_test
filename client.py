
import sys
import xmlrpc.client as client
import time

proxy = client.ServerProxy('http://localhost:9999')
handle = open("./tmp/test.jpg", 'rb')
binary_data = client.Binary(handle.read()).data
start_time = time.time()
proxy.receive_file(binary_data)
print("Time used: ", time.time() - start_time)
handle.close()