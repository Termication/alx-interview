#!/usr/bin/python3
"""
Module for solving the Prime Game problem.
Defines a function to generate prime numbers and determine the game winner.
"""

def primes(n):
    """
    Generate a list of prime numbers between 1 and n (inclusive).

    Args:
        n (int): Upper boundary of the range (inclusive). Lower boundary is always 1.

    Returns:
        list: A list of prime numbers within the range.
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): Number of game rounds.
        nums (list[int]): List of upper limits for each round.

    Returns:
        str: Name of the winner ('Maria' or 'Ben'), or None if there is no winner.
    """
    if x is None or nums is None or x == 0 or not nums:
        return None

    Maria = Ben = 0  # Scores for Maria and Ben

    for i in range(x):
        prime = primes(nums[i])  # Get prime numbers for the current round
        if len(prime) % 2 == 0:  # Ben wins if the count of primes is even
            Ben += 1
        else:  # Maria wins if the count of primes is odd
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
