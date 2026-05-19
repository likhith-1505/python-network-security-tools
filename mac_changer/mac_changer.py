#! usr/bin/env python3

import subprocess

interface = input("Enter the interface ")
new_mac = input("Enter the new mac address ")

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


