#!/usr/bin/python3
"""UTF-8 validation module.
This module provides a function to validate if a given list of integers represents valid UTF-8 encoding.
See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
"""

def validUTF8(data):
    """Determines if a list of integers is valid UTF-8 encoded data.
    
    Each integer represents a byte, and the function validates the encoding
    against the UTF-8 standard, ensuring proper multi-byte sequences.
    
    Args:
        data (list): A list of integers, each representing a byte (0-255).
        
    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise.
    """
    skip = 0  # Number of continuation bytes expected in a multi-byte character
    n = len(data)
    
    for i in range(n):
        if skip > 0:
            # Skip the expected continuation bytes
            skip -= 1
            continue
        
        # Validate byte range and type
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10FFFF:
            return False
        
        # Single-byte (ASCII) character (0xxxxxxx)
        elif data[i] <= 0x7F:
            skip = 0
            
        # 4-byte character encoding (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span:
                # Validate the next three bytes as continuation bytes
                next_body = list(map(lambda x: x & 0b11000000 == 0b10000000, data[i + 1: i + span]))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        
        # 3-byte character encoding (1110xxxx 10xxxxxx 10xxxxxx)
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span:
                # Validate the next two bytes as continuation bytes
                next_body = list(map(lambda x: x & 0b11000000 == 0b10000000, data[i + 1: i + span]))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        
        # 2-byte character encoding (110xxxxx 10xxxxxx)
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span:
                # Validate the next byte as a continuation byte
                next_body = list(map(lambda x: x & 0b11000000 == 0b10000000, data[i + 1: i + span]))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        
        # Invalid UTF-8 encoding
        else:
            return False
    
    return True
