# Fast Port Scanner

A multithreaded port scanner written in Python that allows scanning of multiple ports on a target IP address or hostname.

## Features

- Fast scanning using multithreading
- Customizable port range
- Adjustable timeout for connection attempts
- Colorized output for better readability
- Progress bar to show scanning status
- Option to save results to a file

## Requirements

- Python 3.6+
- colorama

## Installation

1. Clone this repository:   ```
   git clone https://github.com/yourusername/fast-port-scanner.git
   cd fast-port-scanner   ```

2. Install the required packages:   ```
   pip install colorama   ```

## Usage

Run the script with Python:

```
python port_scanner.py [-h] [-s START] [-e END] [-t TIMEOUT] [-T THREADS] [-o OUTPUT] target
```

### Arguments

- `target`: Target IP address or hostname (required)
- `-s`, `--start`: Starting port (default: 1)
- `-e`, `--end`: Ending port (default: 1000)
- `-t`, `--timeout`: Timeout for each connection attempt in seconds (default: 1.0)
- `-T`, `--threads`: Maximum number of threads (default: 100)
- `-o`, `--output`: Output file to save results

### Examples

1. Scan ports 1-1000 on localhost:
   ```
   python port_scanner.py 127.0.0.1
   ```

2. Scan ports 80-443 on example.com with a 2-second timeout:
   ```
   python port_scanner.py example.com -s 80 -e 443 -t 2
   ```

3. Scan ports 1-65535 on 192.168.1.1 using 200 threads and save results to output.txt:
   ```
   python port_scanner.py 192.168.1.1 -s 1 -e 65535 -T 200 -o output.txt
   ```

## How It Works

The Fast Port Scanner uses Python's `concurrent.futures` module to implement multithreading. Here's a brief overview of how it works:

1. The user provides a target IP or hostname and optional parameters for port range, timeout, and thread count.
2. The script resolves the hostname to an IP address if necessary.
3. It creates a thread pool using `ThreadPoolExecutor` with the specified number of threads.
4. The script submits scanning tasks for each port in the specified range to the thread pool.
5. As each port scan completes, the script updates the progress bar and reports open ports.
6. After all ports are scanned, the script displays a summary of open ports and the total scan duration.
7. If specified, the results are saved to an output file.

## Performance Considerations

- Increasing the number of threads can significantly speed up the scanning process, especially for large port ranges.
- Be cautious when scanning networks you don't own or have permission to test, as aggressive scanning may be detected as malicious activity.
- The optimal number of threads depends on your system's capabilities and network conditions. Experiment to find the best balance between speed and reliability.

## Contributing

Contributions to improve the Fast Port Scanner are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with descriptive commit messages
4. Push your changes to your fork
5. Submit a pull request to the main repository

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and testing purposes only. Do not use it to scan networks or systems you do not own or have explicit permission to test. The author is not responsible for any misuse or damage caused by this program.
