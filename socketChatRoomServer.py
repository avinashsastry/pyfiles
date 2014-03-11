# Socket programming based Chat server implementation
# This is a simple chat room implementation:
#  - There are two parts server and client
#  - The point of this excercise is to demonstrate the concept of multiplexing
#    using sockets.

import socket, select

def broadcast_data(sock, message):
    for socket in CONNECTION_LIST:
        if not (socket is sock):
            try:
                socket.send(message)
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)

if __name__ == "__main__":

    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", PORT))
    s.listen(10)

    CONNECTION_LIST.append(s)
    print "Chat server started on port: %s" % PORT

    while True:
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:
            # if new connection is requested, the server socket will be readable
            if sock is s:
                try:
                    sockfd, addr = s.accept()
                except socket.error, msg:
                    print "Failed to connect to client. Error Code: %s, Error message: %s" % (str(msg[0]), str(msg[1])) 

                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected." % addr
                broadcast_data(sockfd, "Client (%s, %s) has entered the room." % addr)
            else:
                try:
                    # Incoming message from a client
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, "\r" + "<" + str(sock.getpeername()) + "> " + data)
                except:
                    broadcast_data(sock, "Client (%s) is offline." % str(sock.getpeername))
                    print "Client (%s) is offline." % str(sock.getpeername)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
    s.close()
