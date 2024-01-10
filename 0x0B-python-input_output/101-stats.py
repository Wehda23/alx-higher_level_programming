#!/usr/bin/python3

"""
Funnier project
"""

import sys
from collections import defaultdict


def print_statistics(file_sizes, status_codes):
    """Statistics"""
    total_size = sum(file_sizes)
    print(f"Total file size: File size: {total_size}")
    sorted_status_codes = sorted(status_codes.keys())

    for code in sorted_status_codes:
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_input_lines():
    """Process"""
    file_sizes = []
    status_codes = defaultdict(int)
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) >= 9:
                file_size = int(parts[-1])
                status_code = parts[-2]
                file_sizes.append(file_size)
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(file_sizes, status_codes)
    except KeyboardInterrupt as e:
        print_statistics(file_sizes, status_codes)


if __name__ == "__main__":
    process_input_lines()
