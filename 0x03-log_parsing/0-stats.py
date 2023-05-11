#!/usr/bin/python3
""" This modules takes input from the sys.stdin and logs it """
import sys
import re


total_size = 0
status_counts = {200: 0,
                 301: 0,
                 400: 0,
                 401: 0,
                 403: 0,
                 404: 0,
                 405: 0,
                 500: 0}
# Define regular expression to match expected line format
pt = r'^(\d+\.\d+\.\d+\.\d+)\s+-\s+\[(.*?)\]\s+'
st = r'"GET /projects/260 HTTP/1\.1"\s+(\d+)\s+(\d+)'
pattern = (pt + st)

# Define the function to print the current metrics
def print_metrics(total_size, status_counts):
    """ We print the metrics """
    print('Total file size:', total_size)
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))


# Process input lines and update metrics
try:
    for i, line in enumerate(sys.stdin):
        # Skip lines that don't match the expected format
        match = re.match(pattern, line.strip())
        if not match:
            continue

        # Extract IP address, date, status code, and file size from the matched
        # line
        ip_address, date, status_code, file_size = match.groups()

        # Update metrics
        total_size += int(file_size)
        status_counts[int(status_code)] += 1

        # Print metrics every 10 lines
        if i > 0 and i % 10 == 0:
            print_metrics(total_size, status_counts)

except KeyboardInterrupt as err:
    # Print final metrics and exit gracefully on keyboard interrupt
    print_metrics(total_size, status_counts)
    print(err)
