#PARIE3
import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12350

msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg, (HOST, PORT))

    data, _ = s.recvfrom(1024)
    print("Réponse du serveur :", data.decode("utf-8"))
#PARTIE4
import socket
import hashlib

HOST = "127.0.0.1"
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(2048)

        try:
            # Séparer message et hash
            message, hash_hex = data.split(b"\x00", 1)

            # Recalculer hash
            calc = hashlib.sha256(message).hexdigest().encode("ascii")

            if calc == hash_hex:
                print("Message valide reçu")
                s.sendto(b"Message et hachage valides", addr)
            else:
                print("Hash invalide")
                s.sendto(b"Erreur de hachage", addr)

        except Exception:
            s.sendto(b"Format invalide", addr)