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
