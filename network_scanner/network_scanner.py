import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered,unanswered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)
    client_list = []
    for elements in answered:
        client_dict = {"ip":elements[1].psrc,"mac":elements[1].hwsrc}
        client_list.append(client_dict)
    return client_list
        
def print_result(result):
    print("IP address \t\t\t Mac Address"+"\n---------------------------------------------------------------")
    for element in result:
        print(element["ip"]+"\t\t"+element["mac"])

result = scan("192.168.122.1/24")
print_result(result)