#!usr/bin/env python3

import argparse
import subprocess

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



parser = argparse.ArgumentParser(
    description="Mac changer"
    )
parser.add_argument(
    "-i","--interface",required=True,help="Interface name"
)
parser.add_argument(
    "-m","--mac",required=True,help="New Mac address"
)
args = parser.parse_args()
change_mac(args.interface,args.mac)


