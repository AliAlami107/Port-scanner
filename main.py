import socket
import threading

# List to store open ports
open_ports = []

# Thread lock for safe access to shared data
thread_lock = threading.Lock()

# Simple port scanner in python

def scan_port(host_port, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    result = sock.connect_ex((host_port, port))
    
    if result == 0:
        with thread_lock:
            open_ports.append(port)
        print(f"Port {port} is open")
    sock.close()

def scan_ports(host_port, start_port, end_port):
    print(f"Scanning ports on {host_port} ")

    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host_port, port))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print the list of open ports after scanning
    if open_ports:
        print("\nOpen Ports: ", open_ports)
    else:
        print("\nNo open ports found.")


if __name__ == "__main__":
    target_hosts = input("Enter the host IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    scan_ports(target_hosts, start_port, end_port)
