import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12350

msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg, (HOST, PORT))

    data, _ = s.recvfrom(1024)
    print("Réponse du serveur :", data.decode("utf-8"))