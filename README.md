# Network_Sniffer
A Python-based network packet sniffer that captures live traffic, displays source/destination IPs, identifies TCP/UDP protocols, and logs packet details. Built for CodeAlpha Cybersecurity Internship Task 1 using Scapy
## Features
- Capture live network packets
- Show source/destination IP addresses  
- Identify TCP/UDP protocols
- Display port numbers and packet size
- Save logs to file

## Requirements
- Python 3.14
- Scapy library

## Installation
   pip install scapy
   
**Run**

   python network_sniffer.py
   
**Output**

   CodeAlpha Network Packet Sniffer
==================================================
Packet limit: 30
--------------------------------------------------

[+] Packet #1
    10.0.33.237:56326 -> 239.255.255.250:1900 [UDP]
    Size: 218 bytes

[+] Packet #2
    10.0.32.46:5353 -> 224.0.0.251:5353 [UDP]
    Size: 127 bytes
.....
.....
    [+] Packet #29
    10.0.33.252:5353 -> 224.0.0.251:5353 [UDP]
    Size: 126 bytes

[+] Packet #30
    10.0.76.201:57522 -> 103.86.38.25:443 [TCP]
    Size: 66 bytes

[+] Done! 30 packets captured.
[+] Log saved to: sniffer_log.txt
