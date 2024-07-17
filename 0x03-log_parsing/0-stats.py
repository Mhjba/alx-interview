#!/usr/bin/python3
'''A script for parsing HTTP request logs and computing metrics.
'''

import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    Args:
        input_line (str): The line of the HTTP request log.

    Returns:
        dict: A dictionary containing extracted information from the log line.
    '''
    # Define regular expressions to extract components of the log line
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    # Construct regex pattern for the entire log line
    log_format = '{}\\-{}{}{}{}\\s*'.format(*log_pattern)
    # Match log line to the pattern
    match = re.fullmatch(log_format, input_line)
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    # If there's a match, extract status code and file size
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    Args:
        total_file_size (int): Total file size.
        status_codes_stats (dict): Dictionary containing counts of
        each status code.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): Current total file size.
        status_codes_stats (dict): Dictionary containing counts of
        each status code.

    Returns:
        int: Updated total file size.
    '''
    # Extract information from the log line
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    # Update status code count
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    # Update total file size
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser.'''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            # Update metrics for each line of input
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            # Print statistics after every 10 lines
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # Print final statistics on interruption or end of file
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
