#!/usr/bin/python3
import sys
import signal

# Initialize counters
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)

# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue
        ip, dash, date, method, url, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
        if not (method == '"GET' and url == '/projects/260' and protocol == 'HTTP/1.1"' and status_code.isdigit() and file_size.isdigit()):
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

