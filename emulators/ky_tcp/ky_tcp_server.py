'''
Created on 15 Jul 2020

@author: IBeRyUS
'''
import socketserver

class ky_tcp_handler(socketserver.BaseRequestHandler):
    def setParent(self, server):
        self.server = server
        
    def handle(self):
        """
        The request handler class for our server.
    
        It is instantiated once per connection to the server, and must
        override the handle() method to implement communication to the
        client.
        """
        # self.request is the TCP socket connected to the client
        
        data = self.request.recv(1024).strip()
        #GpioEmulator.
        #print("{} wrote:".format(self.client_address[0]))
        print(data)
        # just send back the same data, but upper-cased
#        self.request.sendall(self.data.upper())

    def finish(self):
        """
        The request handler class for our server.
    
        It is instantiated once per connection to the server, and must
        override the handle() method to implement communication to the
        client.
        """
        
        print("Peer {} Port {} Disconnected".format(self.client_address[0], self.client_address[1]))
        pass

class ky_tcp_server(socketserver.TCPServer):
    def __init__(self, port_no, emulator):
        self.port_no = port_no
        self.ky_handler = ky_tcp_handler
        super().__init__(("localhost", self.port_no), self.ky_handler)
        self.ky_handler.setParent(self.ky_handler, self)
        self.emulator = emulator

    def service_actions(self):
        #print("ahanda servis aksiyon")
        self.emulator.tickUpdate()
        
'''
    def serve_forever(self):
        with socketserver.TCPServer(("localhost", self.port_no), self.ky_handler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            print("Server Bind on port {}".format(self.port_no))
            server.serve_forever()
'''