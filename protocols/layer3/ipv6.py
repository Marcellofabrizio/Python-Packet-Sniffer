import struct
from protocols.layer3.icmpv6 import ICMPV6
from protocols.layer4.tcp import TCP
from protocols.layer4.udp import UDP

from utils import *
from ..package.protocol import Protocol

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

'''
    IPv6 Header
   |------------------------------------------------------------------------------------------------|
   |           0           |           1           |           2         |            3             | 
   |------------------------------------------------------------------------------------------------|
   |0  1  2  3  4  5  6  7 |8  9 10 11 12 13 14 15 |16 17 18 19 20 21 22 |23 24 25 26 27 28 29 30 31|
   |------------------------------------------------------------------------------------------------|
   |  Version  |      Trafic Class     |                       Flow Label                           |
   |------------------------------------------------------------------------------------------------|
   |                 Payload Lenght                |      Next Head      |         Hop Limit        | 
   |------------------------------------------------------------------------------------------------|
   |                                                                                                |
   |                                                                                                |
   |                                       Source Address                                           |
   |                                                                                                |
   |------------------------------------------------------------------------------------------------|
   |                                                                                                |
   |                                                                                                |
   |                                      Destination Addess                                        |
   |                                                                                                |
   |------------------------------------------------------------------------------------------------|
'''


class IPv6(Protocol):

    def __init__(self, raw_data):
        self.build_package(raw_data)

    def build_package(self, raw_data):
        header = raw_data
        self.version = header[0] >> 4
        self.traffic_class = ((header[0] & 15) << 4) + (header[1] >> 4)
        self.flow_class = ((header[0] & 15) << 8) + header[2]
        self.flow_class = (self.flow_class << 8) + header[3]
        self.payload_len = struct.unpack('! H', header[4:6])
        self.next_header = struct.unpack('! B', header[6:7])
        self.hop_limit = struct.unpack('! B', header[7:8])
        self.data = header[40:]

        self.src_addr = build_ipv6_addr(
            struct.unpack('! 8H', header[8:24])
        )

        self.dest_addr = build_ipv6_addr(
            struct.unpack('! 8H', header[24:40])
        )

        self.next_protocol = self.build_package_data()

    def build_package_data(self):

        if self.next_header == 58:
            return ICMPV6(self.data)

        if self.next_header == 6:
            return TCP(self.data)
        
        if self.next_header == 17:
            return UDP(self.data)

        return None

    def print_data(self):
        print(TAB_1 + 'IPv6 Packet:')

        print(TAB_2 + 'Version: {}, Trafic Class: {}, Flow Label: {}'.format(
            self.version,
            self.traffic_class,
            self.flow_class))

        print(TAB_2 + 'Payload Size: {}, Next Header: {}, Hop Limit: {}'.format(
            self.payload_len,
            self.next_header,
            self.hop_limit))

        print(TAB_2 + 'Source: {}, Target: {}'.format(
              self.src_addr,
              self.dest_addr))

        if self.next_protocol:
            self.next_protocol.print_data()