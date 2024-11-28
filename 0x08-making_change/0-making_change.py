#!/usr/bin/python3
"""Module for determining the minimum number of coins needed to meet a given total."""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins required to achieve a given total.

    Args:
        coins (list): A list of integers representing the values of coins available.
        total (int): The target amount to be achieved.

    Returns:
        int: The minimum number of coins required to achieve the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be achieved with the given coins.
    """
    if total <= 0:
        return 0

    rem = total
    coins_count = 0

    # Sort the coins in descending order for a greedy approach
    sorted_coins = sorted(coins, reverse=True)
    coin_idx = 0
    n = len(coins)

    while rem > 0:
        if coin_idx >= n:
            return -1

        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count
