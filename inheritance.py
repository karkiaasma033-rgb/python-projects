import socket

class Scanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []

    def scan_port(self, port):
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

    def scan_range(self, start, end):
        print(f"\n[*] Scanning {self.target}...")
        for port in range(start, end + 1):
            self.scan_port(port)
        print(f"[*] Open ports: {self.open_ports}")

class AdvancedScanner(Scanner):
    def __init__(self, target):
        super().__init__(target)
        self.vulnerabilities = []

    def check_port_80(self):
        if 80 in self.open_ports:
            self.vulnerabilities.append("Port 80 open - HTTP unencrypted!")
            print("[!] WARNING: Port 80 is open!")
        else:
            print("[+] Port 80 closed - good!")

    def check_port_22(self):
        if 22 in self.open_ports:
            self.vulnerabilities.append("Port 22 open - SSH exposed!")
            print("[!] WARNING: Port 22 open!")
        else:
            print("[+] Port 22 closed - good!")

    def report(self):
        print(f"\n--- SECURITY REPORT for {self.target} ---")
        print(f"Open ports: {self.open_ports}")
        if self.vulnerabilities:
            print("Vulnerabilities found:")
            for v in self.vulnerabilities:
                print(f"  [!] {v}")
        else:
            print("No vulnerabilities found!")

scanner = AdvancedScanner("127.0.0.1")
scanner.scan_range(1, 100)
scanner.check_port_80()
scanner.check_port_22()
scanner.report()
