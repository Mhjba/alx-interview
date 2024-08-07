#!/usr/bin/python3
"""
Task 0. Log parsing

A script that reads stdin line by line and computes metrics.
"""

import re


def extract_input(input_line):
    """ Extracts sections of a line. """
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*', r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_format = '{}\\-{}{}{}{}\\s*'.format(*log_pattern)
    match = re.fullmatch(log_format, input_line)
    lo = {
        'status_code': 0,
        'file_size': 0,
    }
    if match is not None:
        st_code = match.group('status_code')
        fl = int(match.group('file_size'))
        lo['status_code'] = st_code
        lo['file_size'] = fl
    return lo


def print_statistics(total_file_size, status_codes_stats):
    """ Prints the accumulated status"""
    print('File size: {:d}'.format(total_file_size), flush=True)
    for st_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(st_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(st_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """" Updates the metrics. """

    ln = extract_input(line)
    st_code = ln.get('status_code', '0')
    if st_code in status_codes_stats.keys():
        status_codes_stats[st_code] += 1
    return total_file_size + ln['file_size']


def run():
    """ Starts the log parser. """
    Num = 0
    size = 0
    st_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0,
                }
    try:
        while True:
            line = input()
            size = update_metrics(
                line,
                size,
                st_codes,
            )
            Num += 1
            if Num % 10 == 0:
                print_statistics(size, st_codes)
    except (KeyboardInterrupt, EOFError):
        print_statistics(size, st_codes)


if __name__ == '__main__':
    run()
