# PRODIGY_CS_05
Network packet analyzer: Developed a packet sniffer tool that captures and analyzes network packets. The script displays relevant information such as source and destination IP addresses, protocols, and payload data. Ensured the ethical use of the tool for educational purposes.<br><br>
The output of the packet sniffer code will display information about each network packet it captures. Specifically, it will print the source and destination IP addresses, the protocol type, and the payload data. If the packet is a TCP or UDP packet, it will also print the source and destination ports.<br><br>
Here is an example of the expected output:<br><br>
Starting packet sniffer...<br>
Source IP: 192.168.1.2<br>
Destination IP: 192.168.1.1<br>
Protocol: TCP<br>
Source Port: 54321<br>
Destination Port: 80<br>
Payload: b'GET / HTTP/1.1\r\nHost: 192.168.1.1\r\n\r\n'<br>
==================================================<br>
Source IP: 192.168.1.1<br>
Destination IP: 192.168.1.2<br>
Protocol: TCP<br>
Source Port: 80<br>
Destination Port: 54321<br>
Payload: b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html>...</html>'<br>
==================================================<br>
Source IP: 192.168.1.2<br>
Destination IP: 192.168.1.1<br>
Protocol: UDP<br>
Source Port: 12345<br>
Destination Port: 53<br>
Payload: b'\x12\x34\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x05example\x03com\x00\x00\x01\x00\x01'<br>
==================================================<br><br>

This output format provides a clear and structured view of the captured network packets, allowing you to analyze the source and destination of traffic, the protocols in use, and the actual data being transmitted.<br><br>

Some important prerequisites:<br>
1. Install Scapy: Open a terminal (Command Prompt, PowerShell, or the integrated terminal in VS Code) and install scapy using pip: <mark>pip install scapy</mark><br>
2. Run the Script: In the integrated terminal, navigate to the directory containing your packet_sniffer.py file if you aren't already there.<br>
   a) Run the script using Python: <mark>sudo python3 packet_sniffer.py</mark><br>
   b) or for Windows: <mark>python packet_sniffer.py</mark><br><br>

Ethical considerations: <br>
I) Educational Use: Ensure that the tool is used strictly for educational purposes, such as learning about network protocols and packet structures.<br>
II) Legal Compliance: Always obtain permission before sniffing network traffic. Use this tool only on networks you own or have explicit permission to analyze.<br>
III) Data Privacy: Be mindful of the data you capture. Avoid intercepting sensitive or personal information without consent.<br>



