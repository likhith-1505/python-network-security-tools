import scapy.all as scapy

def scan(ip):
    arp_requeste = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_requeste_brodcast = brodcast/arp_requeste
    answered,unanswered = scapy.srp(arp_requeste_brodcast,timeout=1)
    for elements in answered:
        print(elements[0].psrc)
        print(elements[0].hwsrc)

scan("192.168.122.1/24")
