from scapy.all import *
import datetime
import sys

class NetworkSniffer:
    def __init__(self):
        self.packet_count = 0
        self.log_file = "sniffer_log.txt"
        
    def analyze_packet(self, packet):
        self.packet_count += 1
        
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst
            
            if TCP in packet:
                proto = "TCP"
                sport = packet[TCP].sport
                dport = packet[TCP].dport
            elif UDP in packet:
                proto = "UDP"
                sport = packet[UDP].sport
                dport = packet[UDP].dport
            else:
                proto = "OTHER"
                sport = dport = "N/A"
            
            msg = f"\n[+] Packet #{self.packet_count}\n"
            msg += f"    {src}:{sport} -> {dst}:{dport} [{proto}]\n"
            msg += f"    Size: {len(packet)} bytes"
            
            print(msg)
            
            with open(self.log_file, "a") as f:
                f.write(f"{datetime.datetime.now()} | {src} -> {dst} | {len(packet)} bytes\n")
    
    def start_sniffing(self, interface=None, packet_limit=50):
        print("="*50)
        print("CodeAlpha Network Packet Sniffer")
        print("="*50)
        print(f"Packet limit: {packet_limit}")
        print("-"*50)
        
        try:
            sniff(iface=interface, prn=self.analyze_packet, store=False, count=packet_limit)
            print(f"\n[+] Done! {self.packet_count} packets captured.")
            print(f"[+] Log saved to: {self.log_file}")
        except KeyboardInterrupt:
            print(f"\n[+] Stopped. {self.packet_count} packets captured.")

if __name__ == "__main__":
    sniffer = NetworkSniffer()
    sniffer.start_sniffing(packet_limit=30)