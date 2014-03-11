# Simple Chat Server Module written in python

from server import server

class chatServer(server):
    """
    The chatServer class inherits from the server class. 
    Does the following:
        - receives incoming connections
        - groups them into chat rooms, based on the name of the room
        - relays messages from clients in one chat room to all others in the same room
    """

    def __init__(self):
        # Initialize the port and the callback
        port = 5000
        server.__init__(self, port, self.recvConn)

    def welcomeMsg(self, conn):
        conn.send("Welcome to the chat server. \nYou are in the default room. \nType anything you like.")

    # def printMenu(self, conn):
    #     conn.send("\n\n---- Menu Commands ----\n\n")
    #     conn.send("\n1. create_room <room_name> - Creates the room named room_name")
    #     conn.send("\n2. join_room <room_name> - Joins the room room_name")
    #     conn.send("\n3. exit_room - Exits the room and closes the connection")

    def recvConn(self, conn):
        """
        Receives and handles incoming connections from clients
        """
        self.welcomeMsg(conn)
        # self.printMenu(conn)
        
        conn.send("\nType \"bye\" to exit.")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            if data == "bye":
                break

            if not self.connList:
                print "Error - No connections registered - closing connection."
                break;

            for clientConn in self.connList:
                if not (clientConn is conn):
                    clientConn.sendall(data)

        self.removeConn(conn)

c = chatServer()
c.run()