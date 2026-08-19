import socket

host = input("Target host: ")
n = int(input("How many ports to scan: "))

print(f"\nScanning {host} ports 1 to {n}...\n")

for port in range(1, n + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    s.close()

print("\nScan finished.")