import scapy.all as scapy

def scan(ip):
    scapy.arpping(ip)

scan("192.168.122.1/24")