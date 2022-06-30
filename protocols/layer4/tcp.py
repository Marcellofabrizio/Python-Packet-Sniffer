import struct
from ..package.protocol import Protocol
from protocols.layer5.http import HTTP
from utils import *

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '

class TCP(Protocol):

    def __init__(self, raw_data):
        self.build_package(raw_data)

    def build_package(self, raw_data):
        (self.src_port, self.dest_port, self.sequence, self.acknowledgment, offset_reserved_flags) = struct.unpack(
            '! H H L L H', raw_data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        self.flag_urg = (offset_reserved_flags & 32) >> 5
        self.flag_ack = (offset_reserved_flags & 16) >> 4
        self.flag_psh = (offset_reserved_flags & 8) >> 3
        self.flag_rst = (offset_reserved_flags & 4) >> 2
        self.flag_syn = (offset_reserved_flags & 2) >> 1
        self.flag_fin = offset_reserved_flags & 1
        self.data = raw_data[offset:]

        self.next_protocol = self.build_package_data()

    def build_package_data(self):
        if len(self.data) > 0:
                # HTTP
                print(self.src_port, self.dest_port)
                if self.src_port == 80 or self.dest_port == 80:
                    return HTTP(self.data)
        
        return None


    def print_data(self):
        print(TAB_1 + 'TCP Segment:')
        print(TAB_2 + 'Source Port: {}, Destination Port: {}'.format(self.src_port, self.dest_port))
        print(TAB_2 + 'Sequence: {}, Acknowledgment: {}'.format(self.sequence, self.acknowledgment))
        print(TAB_2 + 'Flags:')
        print(TAB_3 + 'URG: {}, ACK: {}, PSH: {}'.format(self.flag_urg, self.flag_ack, self.flag_psh))
        print(TAB_3 + 'RST: {}, SYN: {}, FIN:{}'.format(self.flag_rst, self.flag_syn, self.flag_fin))
