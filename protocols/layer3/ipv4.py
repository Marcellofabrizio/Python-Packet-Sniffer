import struct
from utils import *

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

class IPv4:

    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.ttl, self.proto, src, target = struct.unpack(
            '! 8x B B 2x 4s 4s', raw_data[:20])
        self.src = build_ipv4_addr(src)
        self.target = build_ipv4_addr(target)
        self.data = raw_data[self.header_length:]

    def __str__(self):
        print(TAB_1 + 'IPv4 Packet:')
        print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(self.version, self.header_length, self.ttl))
        print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(self.proto, self.src, self.target))
