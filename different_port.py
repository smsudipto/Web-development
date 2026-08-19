#!/usr/bin/env python3
import socket

host = input("Target host: ").strip()
port = int(input("Target port (e.g. 443): ").strip())
n = int(input("How many connections to open: ").strip())

print(f"\nOpening {n} connections to {host}:{port}...\n")

sockets = []
for i in range(1, n + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        local_ip, local_port = s.getsockname()
        remote_ip, remote_port = s.getpeername()
        print(f"[Connection {i}] local {local_ip}:{local_port} -> remote {remote_ip}:{remote_port}")
        sockets.append(s)
    except Exception as e:
        print(f"[Connection {i}] failed: {e}")

input("\nPress Enter to close all connections...")

for s in sockets:
    s.close()

print("Done.")