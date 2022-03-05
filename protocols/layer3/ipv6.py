import struct


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


class IPv6:

    def __init__(self, raw_data):
        header = raw_data
        self.version = header[0] >> 4
        self.traffic_class = ((header[0] & 15) << 4) + (header[1] >> 4)
        self.flow_class = ((header[0] & 15) << 8) + header[2]
        self.flow_class = (self.flow_class << 8) + header[3]
        self.payload_len = struct.unpack('! H', header[4:6])
        self.next_header = struct.unpack('! B', header[6:7])
        self.hop_limit = struct.unpack('! B', header[7:8])

        self.src_addr = self.build_ipv6_addr(
            struct.unpack('! 8H', header[8:24])
        )

        self.dest_addr = self.build_ipv6_addr(
            struct.unpack('! 8H', header[24:40])
        )

    def build_ipv6_addr(self, addr_data):
        '''
        Returns properly formatted IPv6 address
        '''
        return ':'.join(map('{:04x}'.format, addr_data))
