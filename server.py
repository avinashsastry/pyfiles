# Object oriented implementation of a server. The server will handle the following:
#   - Create a socket
#   - Open and listen on a port
   
import socket
import sys
from thread import *

class server:
    def __init__(self, port, client_fn):
        """
        init takes in the port on which the server will be opened.
        hostname is localhost always.
        client_fn is a callback that will be called by a class that inherits server.

        init does:
            - Create a socket and bind it to the port
        """
        self.HOST = '' # Symbolic name meaning all available interfaces
        self.PORT = port 
        self.client_fn = client_fn
        self.initComplete = False

        # Keep a record of the open connections
        self.connList = []

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print "Socket created."
            self.s.bind((self.HOST, self.PORT))
            print "Bind Success"
            self.initComplete = True
        except socket.error, msg:
            print "Socket binding failed. Error Code: %s, Error message: %s" % (str(msg[0]), str(msg[1]))

    def closeSocket(self):
        """
        Close the socket, if init has been called.
        """
        if not self.initComplete:
            return
        self.s.close()

    def registerConn(self, conn, addr):
        """
        Maintain a registry of open connections at any given time
        """
        self.connList.append(conn)
        print "Registered conn from address: %s:%s" % (addr[0], addr[1])

    def removeConn(self, conn):
        """
        De-register a connection
        """
        self.connList.remove(conn)
        conn.close()
        print "Client connection closed."

    def run(self):
        """
        Function to start listening on the open port and handle incoming connections
        """
        if not self.initComplete:
            print "Init failed. Please restart the server."
            self.closeSocket()
            return

        if not self.client_fn:
            print "Connection callback has not been set. Stopping the server."
            self.closeSocket()
            return

        # Time to start listening
        self.s.listen(10) 
        print "Listening on %s:%s" % (self.HOST, self.PORT)

        while True:
            conn, addr = self.s.accept()
            self.registerConn(conn, addr)
            print "Connected with %s:%s" % (addr[0], addr[1])
            start_new_thread(self.client_fn, (conn, ))

        closeSocket()






