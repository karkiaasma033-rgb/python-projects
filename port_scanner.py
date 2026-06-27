import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex ((host, port))
        sock.close()
        if result == 0:
            print(f"Port {port} is OPEN")
    except:
        pass

def scan_host(host, start_port, end_port):
    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)
    print("\nScan complete!")

host = input("Enter host to scan (e.g. 127.0.0.1): ")
start = int(input("Start port:"))
end = int(input("End port: "))

scan_host(host, start, end)



