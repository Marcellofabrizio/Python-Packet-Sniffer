import re
from ..package.protocol import Protocol

# https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_for_IPv6

class ICMPV6(Protocol):

    def __init__(self, raw_data):
        self.build_package(raw_data)

    def build_package(self, raw_data):
        header = raw_data
        self.icmpv6_data = header[:8]
        self.type = header[0]
        self.code = header[1]
        self.checksum = header[2:4]
        self.message_body = self.icmpv6_data[4:8]
        self.data = raw_data[8:]

    def print_data(self):
        print('\t - ICMPv6 Packet:\n')
        print(f'\t\t - Type: {self.type}, Type Name: {ICMPV6Messages.get_type_message(self.type)}\n')
        print(f'\t\t - Code: {self.code}')
        try:
            result = f'\t\t - Code Name: {ICMPV6Messages.get_code(self.type)[self.code]}\n'
            print(result)
        except:
            print('\n')
        print('\t\t - Checksum: {self.checksum}\n')
        print('\t\t - ICMPv6 Data: {self.data}\n')

class ICMPV6Messages():

    def __init__(self):

        self.icmp6_types = {
            1: "Destination unreachable",
            2: "Packet too big",
            3: "Time exceeded",
            4: "Parameter problem",
            100: "Private Experimentation",
            101: "Private Experimentation",
            128: "Echo Request",
            129: "Echo Reply",
            130: "MLD Query",
            131: "MLD Report",
            132: "MLD Done",
            133: "Router Solicitation",
            134: "Router Advertisement",
            135: "Neighbor Solicitation",
            136: "Neighbor Advertisement",
            137: "Redirect Message",
            138: "Router Renumbering",
            139: "ICMP Node Information Query",
            140: "ICMP Node Information Response",
            141: "Inverse Neighbor Discovery Solicitation Message",
            142: "Inverse Neighbor Discovery Advertisement Message",
            143: "MLD Report Version 2",
            144: "Home Agent Address Discovery Request Message",
            145: "Home Agent Address Discovery Reply Message",
            146: "Mobile Prefix Solicitation",
            147: "Mobile Prefix Advertisement",
            148: "Certification Path Solicitation",
            149: "Certification Path Advertisement",
            151: "Multicast Router Advertisement",
            152: "Multicast Router Solicitation",
            153: "Multicast Router Termination",
            155: "RPL Control Message",
            200: "Private Experimentation",
            201: "Private Experimentation"
        }

        self.icmp6_codes = {
        
            1: {
                0: "No route to destination",
                1: "Communication with destination administratively prohibited",
                2: "Beyond scope of source address",
                3: "Address unreachable",
                4: "Port unreachable",                    
                5: "source address failed ingress/egress policy",
                6:	"reject route to destination",
                7:	"Error in Source Routing Header"
            },
            3: {
                0: 'hop limit exceeded in transit',
                1: 'fragment reassembly time exceeded'
            },
            4: {
                0: 'erroneous header field encountered',
                1: 'unrecognized Next Header type encountered',
                2: 'unrecognized IPv6 option encountered'
            },
            138: {
                0: 'Router Renumbering Command',
                1:	'Router Renumbering Result',
                255: 'Sequence Number Reset'
            },
            139: {
                0: 'The Data field contains an IPv6 address which is the Subject of this Query.',
                1: 'The Data field contains a name which is the Subject of this Query, or is empty, as in the case of a NOOP.',
                2: 'The Data field contains an IPv4 address which is the Subject of this Query.' 
            }
        } 

    @staticmethod
    def get_type_message(self, type):
        return self.icmp6_types[type]

    @staticmethod
    def get_code(self, type):
        return self.icmp6_codes[type]
