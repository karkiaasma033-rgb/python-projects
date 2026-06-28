import socket

class NetworkScanner:
    def __init__(self, host):
        self.host = host
        self.open_ports = []

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.host, port))
            sock.close()
            if result == 0:
                self.open_ports.append(port)
                print(f"Port {port} is OPEN")
        except:
            pass

    def scan_range(self, start, end):
        print(f"\nScanning {self.host}...\n")
        for port in range(start, end + 1):
            self.scan_port(port)
        print(f"\nFound {len(self.open_ports)} open ports: {self.open_ports}")

scanner = NetworkScanner("127.0.0.1")
scanner.scan_range(1, 100)

