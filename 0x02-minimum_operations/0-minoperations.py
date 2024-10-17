#!/usr/bin/python3
'''Minimum Operations Python 3 Challenge'''


def minOperations(n):
    '''Calculate the fewest number of operations needed to 
    achieve exactly n 'H' characters in a file.
    
    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required to reach 
        exactly n characters, or 0 if it's impossible.
    '''
    current_chars = 1  # Current number of 'H' characters in the file
    copied_chars = 0  # Number of 'H' characters in the clipboard
    operation_count = 0  # Total number of operations performed

    while current_chars < n:
        # If no characters have been copied yet
        if copied_chars == 0:
            # Copy all current characters to clipboard
            copied_chars = current_chars
            # Increment operation count
            operation_count += 1

        # If only one character is currently in the file
        if current_chars == 1:
            # Paste from clipboard
            current_chars += copied_chars
            # Increment operation count
            operation_count += 1
            continue  # Proceed to the next iteration

        remaining_chars = n - current_chars  # Remaining characters needed to reach n

        # If the clipboard has more characters than needed, achieving n is impossible
        if remaining_chars < copied_chars:
            return 0

        # If the remaining characters cannot be evenly divided by the current number of 'H' characters
        if remaining_chars % current_chars != 0:
            # Paste current clipboard contents
            current_chars += copied_chars
            # Increment operation count
            operation_count += 1
        else:
            # Copy all current characters to clipboard
            copied_chars = current_chars
            # Paste from clipboard
            current_chars += copied_chars
            # Increment operation count for both operations
            operation_count += 2

    # Check if the desired number of characters has been achieved
    return operation_count if current_chars == n else 0
