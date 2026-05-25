import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    client_list = []
    for elements in answered:
        client_dict = {"ip": elements[1].psrc, "mac": elements[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(result):
    print(
        "IP address \t\t\t Mac Address"
        + "\n---------------------------------------------------------------"
    )
    for element in result:
        print(element["ip"] + "\t\t" + element["mac"])


ip = input("Enter IP range (example: 192.168.1.1/24): ")
result = scan(ip)
print_result(result)
