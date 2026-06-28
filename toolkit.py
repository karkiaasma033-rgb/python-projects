import socket
import hashlib

class HackingToolkit:
    def __init__(self, target):
        self.target = target
        self.open_ports = []

    def port_scan(self, start, end):
        print(f"\n[*] Scanning ports on {self.target}...")
        for port in range(start, end + 1):
            try:
                 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                 sock.settimeout(1)
                 result = sock.connect_ex((self.target, port))
                 sock.close()
                 if result == 0:
                    self.open_ports.append(port)
                    print(f"[+] Port {port} is OPEN")
            except:
                pass
        print(f"[*] Scan complete! Open ports: {self.open_ports}")

    def hash_text(self, text):
        print(f"\n[*] Hashing: {text}")
        md5 = hashlib.md5(text.encode()).hexdigest()
        sha256 = hashlib.sha256(text.encode()).hexdigest()
        print(f"[+]  MD5: {md5}")
        print(f"[+] SHA256: {sha256}")

    def check_password(self, password):
        print(f"/n[*] Checking password strength...")
        score = 0
        if len(password) >= 8: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in "!@#$%^&*" for c in password): score += 1
        strength = "STRONG" if score == 5 else "MEDIUM" if score >= 3 else "WEAK"
        print(f"[+] Password strength: {strength} ({score}/5")

#Create toolkit
toolkit = HackingToolkit("127.0.0.1")

while True:
    print("/n1. Port Scan 2. Hash Text 3. Check Password 4. Quit")
    choice = input("Choose: ")
    if choice == "1":
        toolkit.port_scan(1, 100)
    elif choice == "2":
        text = input("Enter text to hash: ")
        toolkit.hash_text(text)
    elif choice == "3":
        pwd = input("Enter password: ")
        toolkit.check_password(pwd)
    elif choice == "4":
        break
