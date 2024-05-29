import scapy.all as scapy

# Function to process captured packets
def process_packet(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        payload = packet[scapy.Raw].load if packet.haslayer(scapy.Raw) else None

        print(f"[*] Source IP: {ip_src} --> Destination IP: {ip_dst} | Protocol: {protocol}")
        if payload:
            print("[+] Payload:")
            print(payload)

# Function to start packet sniffing
def sniff_packets(interface):
    print("[*] Starting packet sniffing...")
    scapy.sniff(iface=interface, prn=process_packet, store=False)

# Main function
def main():
    interface = input("Enter the interface to sniff (e.g., eth0): ")
    sniff_packets(interface)

if __name__ == "__main__":
    main()