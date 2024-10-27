#!/usr/bin/python3
'''A script that generates random HTTP request logs.

This script simulates HTTP requests by generating random log entries with
randomized IP addresses, HTTP status codes, and response sizes. It outputs 
these log entries to the standard output, simulating a log file.
'''
import random
import sys
import datetime
from time import sleep


# Generate 10,000 random HTTP request log entries
for i in range(10000):
    # Introduce a random delay between log entries
    sleep(random.random())

    # Generate a log entry with random data and print it to stdout
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} {}\" {} {}\n".format(
        random.randint(1, 255),     # Random first byte of IP address
        random.randint(1, 255),     # Random second byte of IP address
        random.randint(1, 255),     # Random third byte of IP address
        random.randint(1, 255),     # Random fourth byte of IP address
        datetime.datetime.now(),    # Current timestamp
        '/projects/1216',           # Requested URL (static in this case)
        'HTTP/1.1',                 # HTTP version
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),  # Random HTTP status code
        random.randint(1, 1024)     # Random response size (in bytes)
    ))
    
    # Ensure the log entry is immediately written to stdout
    sys.stdout.flush()
