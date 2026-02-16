
from pathlib import Path
p = Path("data/message.txt") 
s = p.read_text(encoding="utf-8") 
print(type(s), len(s)) 
print(s)
b = p.read_bytes() 
print(type(b), len(b)) 
print(b[:20]) 

b2 = s.encode("utf-8") 
s2 = b.decode("utf-8") 
print(len(b2), type(b2)) 
print(type(s2))  


import socket

HOST = "127.0.0.1"
PORT = 12350

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP en écoute sur {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)

        print(f"Reçu {len(data)} octets de {addr}")
        print("Message :", data.decode("utf-8", errors="replace"))

        s.sendto(b"Message recu", addr)