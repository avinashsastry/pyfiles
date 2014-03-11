# Socket programming example in Python
import socket
import sys

try:
    # create an AF_INET (IPv4) and SOCK_STREAM (TCP) socket.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Failed to create socket. Error Code: %s, Error Message: %s" % (str(msg[0]), str(msg[1]))
    sys.exit()

print "Socket Created."

# The next step is to connect to some server

host = "www.google.com"
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    #could not resolve error
    print "Host name %s could not be resolved to an IP address." % host
    sys.exit()

print "IP Address of host \"%s\" is %s" % (host, remote_ip)

s.connect((remote_ip, port))

print "Connected to %s (%s) on port %s" % (host, remote_ip, port)

# time to request some data from google
message = "GET / HTTP/1.1\r\n\r\n"
try: 
    s.sendall(message)
except socket.error:
    print "Sending Failed."
    sys.exit()

print "Message sent."

# time to receive the response from google
# 4096 is the buffer size
r = s.recv(4096)

print r

s.close()