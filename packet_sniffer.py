from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        proto_name = 'UNKNOWN'
        if proto == 6:
            proto_name = 'TCP'
        elif proto == 17:
            proto_name = 'UDP'
        
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {proto_name}")

        if proto == 6 and TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        elif proto == 17 and UDP in packet:
            udp_layer = packet[UDP]
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        print(f"Payload: {bytes(packet[IP].payload)}")
        print("="*50)

def main():
    # Start sniffing packets
    print("Starting packet sniffer...")
    sniff(filter="ip", prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
