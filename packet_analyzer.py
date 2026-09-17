from scapy.all import sniff, IP, TCP, UDP, ICMP


def analyze_packet(packet):
    print("\n" + "=" * 50)

    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        print("Source IP      :", source_ip)
        print("Destination IP :", destination_ip)

        if TCP in packet:
            print("Protocol       : TCP")
            print("Source Port    :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol       : UDP")
            print("Source Port    :", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif ICMP in packet:
            print("Protocol       : ICMP")

        else:
            print("Protocol       : Other")

        print("Packet Size    :", len(packet), "bytes")

    else:
        print("Non-IP packet")

    print("=" * 50)


print("Starting Network Packet Analyzer...")
print("Capturing packets... Press CTRL+C to stop.")

sniff(prn=analyze_packet, store=False)
