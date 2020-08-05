'''
Created on 5 Aug 2020

@author: IBeRyUS
'''
from ky_tcp_server import ky_tcp_server

class gpioEmulator(object):
    '''
    classdocs
    '''
    def tickUpdate(self):
        print("Tick Update")
        
    def __init__(self):
        '''
        Constructor
        '''
        self.port_num = 9999
        self.connection = ky_tcp_server(self.port_num, self)
#        self.tcp.ky_handler.getParent(self.tcp.ky_handler, self)
        self.connection.serve_forever()


                