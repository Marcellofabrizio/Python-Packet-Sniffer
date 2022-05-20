import socket
import struct
from utils import *
from ..package.protocol import Protocol

class Ethernet(Protocol):

    def __init__(self, raw_data):

        self.build_package(raw_data)

    def build_package(self, raw_data):
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

        self.dest_mac = get_mac_addr(dest)
        self.src_mac = get_mac_addr(src)
        self.proto = socket.htons(prototype)
        self.data = raw_data[14:]
    
    __str__(self):        
        print('\nEthernet Frame:')
        print('\t - Destination: {}, Source: {}, Protocol: {}'.format(self.dest_mac, self.src_mac, self.proto))
