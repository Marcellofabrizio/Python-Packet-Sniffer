import struct
from protocols.layer3.icmp import ICMP
from protocols.layer4.tcp import TCP
from protocols.layer4.udp import UDP

from utils import *
from ..package.protocol import Protocol


TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '


class IPv4(Protocol):

    def __init__(self, raw_data):
        self.build_package(raw_data)

    def build_package(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.ttl, self.proto, src, target = struct.unpack(
            '! 8x B B 2x 4s 4s', raw_data[:20])
        self.src = build_ipv4_addr(src)
        self.target = build_ipv4_addr(target)
        self.data = raw_data[self.header_length:]

        self.next_protocol = self.build_package_data()

    def build_package_data(self):

        self.next_protocol = None

        if self.proto == 1:
            return ICMP(self.data)

        if self.proto == 6:
            return TCP(self.data)

        if self.proto == 17:
            return UDP(self.data)

        return None

    def print_data(self):
        print(TAB_1 + 'IPv4 Packet:')
        print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(self.version,
              self.header_length, self.ttl))
        print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(self.proto,
              self.src, self.target))

        print(self.next_protocol)
        if self.next_protocol is not None:
            self.next_protocol.print_data()

        else:
            print(TAB_1 + 'Other IPv4 Data Protocol :')
            print(format_multi_line('TAB_2',self.data))
        
