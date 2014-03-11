# Socket programming in python to create a simple server
import socket
import sys
from thread import *

# create a new function to handle connections from each client
# This function will be called on a new thread so that multiple clients
# can talk to the server at the same time.
def clientthread(conn):
    # Send a welcome message
    conn.send("Welcome to the server. Type a message to have it bounced back to you")
    while True:
        data = conn.recv(1024)
        reply = "OK... " + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()


HOST = '' # Symbolic name meaning all available interfaces
PORT = 5000  # this is a non-privileged PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created."

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print "Socket binding failed. Error Code: %s, Error message: %s" % (str(msg[0]), str(msg[1]))
    sys.exit()

print "Bind Success!"

# Time to start listening
s.listen(10) # Here the argument is the backlog - the number of connections that will be held till the next one is rejected.
print "Listening on %s:%s" % (HOST, PORT)

while 1:
    conn, addr = s.accept()
    print "Connected with %s:%s" % (addr[0], addr[1])
    start_new_thread(clientthread, (conn, ))

s.close()