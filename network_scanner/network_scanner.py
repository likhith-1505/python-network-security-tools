import scapy.all as scapy

def scan(ip):
    arp_requeste = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_requeste_brodcast = brodcast/arp_requeste
    arp_requeste_brodcast.show()
scan("192.168.122.1/24")