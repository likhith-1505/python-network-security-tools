#!usr/bin/env python3

import argparse
import subprocess
import re
def change_mac(interface,new_mac):
    print(f"[+] The mac address of {interface} is changed to {new_mac}")

    subprocess.run([
        "sudo","ip","link","set","dev",interface,"down"
        ],check=True)

    subprocess.run([
        "sudo","ip","link","set","dev",interface,"address",new_mac
        ],check=True)

    subprocess.run([
        "sudo","ip","link","set","dev",interface,"up"
        ],check=True)
def get_arguments():
    parser = argparse.ArgumentParser(
        description="Mac changer"
    )
    parser.add_argument(
        "-i","--interface",required=True,help="Interface name"
    )
    parser.add_argument(
        "-m","--mac",required=True,help="New Mac address"
    )
    return parser.parse_args()



args = get_arguments()
change_mac(args.interface,args.mac)
result = subprocess.check_output(
    ["ip", "addr", "show", args.interface],
    text=True
)
current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",result)

if current_mac:
    if current_mac.group(0) == args.mac:
        print(f"[+] Mac changed successfully")
    else:
        print(f"[-] Mac address is not changed")
else:
    print("Mac address can't be read")
    
