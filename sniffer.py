import socket

from protocols import Ethernet
from pcap import Pcap
from socket import socket, AF_PACKET, SOCK_RAW, ntohs

def main():
    pcap = Pcap('capture.pcap')
    conn = socket(AF_PACKET, SOCK_RAW, ntohs(3))

    while True:
        raw_data = conn.recvfrom(65535)[0]
        pcap.write(raw_data)
        eth = Ethernet(raw_data)
        eth.print_data()

main()
