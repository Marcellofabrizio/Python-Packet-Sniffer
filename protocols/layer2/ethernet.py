import socket
import struct
from utils import *
from ..package.protocol import Protocol

from protocols.layer2.arp import ARP
from protocols.layer3.ipv4 import IPv4
from protocols.layer3.ipv6 import IPv6

ARP_TYPE = int("0x0608", 16)
IPV4_TYPE = 8
IPV6_TYPE = int("0xDD86", 16)

DATA_TAB_1 = '\t   '

class Ethernet(Protocol):

    def __init__(self, raw_data):

        self.build_package(raw_data)

    def build_package(self, raw_data):
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

        self.dest_mac = get_mac_addr(dest)
        self.src_mac = get_mac_addr(src)
        self.proto = socket.htons(prototype)
        self.data = raw_data[14:]
    
        self.next_protocol = self.build_package_data(raw_data)

    def build_package_data(self, raw_data):

        if self.proto == ARP_TYPE:
            return ARP(raw_data)
            
        elif self.proto == IPV4_TYPE:
            return IPv4(self.data)
        
        elif self.proto == IPV6_TYPE:
            return IPv6(self.data)

        return None

    def print_data(self):        
        print('\nEthernet Frame:')
        print('\t - Destination: {}, Source: {}, Protocol: {}'.format(self.dest_mac, self.src_mac, self.proto))

        if self.next_protocol:
            self.next_protocol.print_data()

        else: 
            print('Ethernet Data:')
            print(format_multi_line(DATA_TAB_1, self.data))