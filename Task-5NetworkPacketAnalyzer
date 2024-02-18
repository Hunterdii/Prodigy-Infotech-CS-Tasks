import scapy.all as scapy

def packet_sniffer(packet):
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(f"Source IP: {source_ip}  Destination IP: {destination_ip}  Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Payload: {payload}")

def main(interface):
    scapy.sniff(iface=interface, prn=packet_sniffer, store=False)

if __name__ == "__main__":
    interface = input("Enter the interface to sniff (e.g., eth0): ")
    main(interface)
