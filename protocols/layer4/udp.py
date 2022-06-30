import struct
from ..package.protocol import Protocol

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '
class UDP(Protocol):

    def __init__(self, raw_data):
        self.build_package(raw_data)

    def build_package(self, raw_data):
        self.src_port, self.dest_port, self.size = struct.unpack('! H H 2x H', raw_data[:8])
        self.data = raw_data[8:]

    def print_data(self):
        print(TAB_1 + 'UDP Segment:')
        print(TAB_2 + 'Source Port: {}, Destination Port: {}, Length: {}'.format(self.src_port, self.dest_port, self.size))