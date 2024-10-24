import argparse
import socket
import threading
import concurrent.futures
import time
from colorama import Fore, Style, init

init(autoreset=True)

def scan_port(ip, port, timeout):
    try:
        with socket.create_connection((ip, port), timeout=timeout) as sock:
            return port, True
    except (socket.timeout, ConnectionRefusedError):
        return port, False
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return port, False

def scan_ports(ip, start_port, end_port, timeout, max_threads):
    open_ports = []
    total_ports = end_port - start_port + 1
    scanned_ports = 0

    print(f"\nScanning {ip} from port {start_port} to {end_port}")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_port = {executor.submit(scan_port, ip, port, timeout): port for port in range(start_port, end_port + 1)}
        
        for future in concurrent.futures.as_completed(future_to_port):
            port, is_open = future.result()
            scanned_ports += 1
            progress = (scanned_ports / total_ports) * 100
            print(f"\rProgress: [{('=' * int(progress // 2)).ljust(50)}] {progress:.1f}%", end="", flush=True)
            
            if is_open:
                open_ports.append(port)
                print(f"\n{Fore.GREEN}[+] Port {port} is open{Style.RESET_ALL}")

    end_time = time.time()
    duration = end_time - start_time
    print(f"\n\nScan completed in {duration:.2f} seconds")
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Fast Port Scanner with Multithreading")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Starting port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1000, help="Ending port (default: 1000)")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout for each connection attempt (default: 1.0)")
    parser.add_argument("-T", "--threads", type=int, default=100, help="Maximum number of threads (default: 100)")
    parser.add_argument("-o", "--output", help="Output file to save results")

    args = parser.parse_args()

    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{args.target}'")
        return

    open_ports = scan_ports(ip, args.start, args.end, args.timeout, args.threads)

    if open_ports:
        print(f"\nOpen ports on {ip}:")
        for port in open_ports:
            print(f"  - {port}")
    else:
        print(f"\nNo open ports found on {ip}")

    if args.output:
        with open(args.output, "w") as f:
            f.write(f"Scan results for {ip}:\n")
            if open_ports:
                f.write("Open ports:\n")
                for port in open_ports:
                    f.write(f"  - {port}\n")
            else:
                f.write("No open ports found\n")
        print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    main()
