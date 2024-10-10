def canUnlockAll(boxes):
    '''Determines if all boxes can be unlocked.'''
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is always unlocked

    keys = [0]  # Start with the keys from the first box

    # Iterate through the keys and unlock boxes
    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  # Check if the key is valid and the box is not already unlocked
                unlocked[key] = True
                keys.append(key)  # Add the keys from the newly unlocked box

    return all(unlocked)  # Check if all boxes are unlocked
