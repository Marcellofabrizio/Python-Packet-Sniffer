import socket
import struct
from utils import *

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '


class ARP:

    def __init__(self, raw_data):
        header = raw_data[14:42]

        self.hrdwr_type = struct.unpack("! H", header[0:2])[0]
        self.proto_type = struct.unpack("! H", header[2:4])[0]
        self.hrdwr_addr_len = struct.unpack("! B", header[4:5])[0]
        self.proto_len = struct.unpack("! B", header[5:6])[0]
        self.opcode = struct.unpack("! H", header[6:8])[0]
        self.sender_mac_addr = struct.unpack("! 6s", header[8:14])[0]
        self.sender_ip_addr = struct.unpack("! 4s", header[14:18])[0]
        self.dest_mac_addr = struct.unpack("! 6s", header[18:24])[0]
        self.dest_ip_addr = struct.unpack("! 4s", header[24:28])[0]

    def print_arp_data(self):

        print(TAB_1 + "ARP Packet:")

        print(TAB_2 + "Hardware Type: {}, Protocol Type: {}, Operation Code: {}".format(self.hrdwr_type,
                                                                                        self.proto_type,
                                                                                        self.opcode))

        print(TAB_2 + "Sender MAC Address: {}, Sender IP Address: {}".format(get_mac_addr(self.sender_mac_addr),
                                                                             build_ipv4_addr(self.sender_ip_addr)))

        print(TAB_2 + "Destination MAC Address: {}, Destination IP Address: {}".format(get_mac_addr(self.dest_mac_addr),
                                                                               build_ipv4_addr(self.dest_ip_addr)))
