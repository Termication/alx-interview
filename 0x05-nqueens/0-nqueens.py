#!/usr/bin/env python3
"""
N-Queens puzzle solver.
This script places N non-attacking queens on an N×N chessboard.
"""
import sys


def print_usage_and_exit(message):
    """Prints an error message, usage guidance, and exits with status 1."""
    print(message)
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col].
    Ensures no queen in the same column, or diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, board=[], solutions=[]):
    """
    Recursively places queens on the board to find all solutions.
    
    Args:
        n (int): Size of the board and number of queens.
        row (int): Current row being processed.
        board (list): Current board configuration.
        solutions (list): Stores all valid solutions.
    """
    if row == n:
        # Each solution is represented as a list of [row, col] positions.
        solutions.append([[i, board[i]] for i in range(n)])
        return
    
    for col in range(n):
        if is_valid(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Incorrect number of arguments.")
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number.")
    
    if n < 4:
        print_usage_and_exit("N must be at least 4.")
    
    solutions = []
    solve_nqueens(n, 0, [], solutions)
    
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
