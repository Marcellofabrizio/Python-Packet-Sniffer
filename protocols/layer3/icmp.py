import struct
from utils import *
from ..package.protocol import Protocol

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

class ICMP(Protocol):

    def __init__(self, raw_data):
        self.build_package(raw_data)

    def build_package(self, raw_data):
        self.type, self.code, self.checksum = struct.unpack(
            '! B B H', raw_data[:4])
        self.data = raw_data[4:]

    def print_data(self):
        print(TAB_1 + 'ICMP Packet:')
        print(TAB_2 + 'Type: {}, Code: {}, Checksum: {},'.format(self.type, self.code, self.checksum))
        print(TAB_2 + 'ICMP Data:')
        print(format_multi_line('\t\t\t   ', self.data))