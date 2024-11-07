#!/usr/bin/python3
"""
N-Queens Solution Finder
This module solves the N-Queens puzzle by finding all valid arrangements
where N queens can be placed on an NxN
chessboard without threatening each other.
"""
import sys

solutions = []
"""List to store possible solutions for the N-Queens problem."""
n = 0
"""Size of the chessboard (NxN)."""
positions = None
"""List representing all possible positions on the chessboard."""


def parse_and_validate_input():
    """
    Parses and validates the command-line argument for the board size.

    Returns:
        int: The size of the chessboard, n.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def queens_are_attacking(pos0, pos1):
    """
    Checks if two queens are in an attacking position.

    Args:
        pos0 (list[int, int]): Position of the first queen [row, col].
        pos1 (list[int, int]): Position of the second queen [row, col].

    Returns:
        bool: True if the queens are in an attacking position; otherwise False.
    """
    # Queens attack if they share the same row, column, or diagonal.
    return (
        pos0[0] == pos1[0]
        or pos0[1] == pos1[1]  # Same row
        or abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])  # Same column
    )  # Same diagonal


def solution_is_unique(candidate_solution):
    """
    Checks if a similar solution already exists in the solutions list.

    Args:
        candidate_solution (list[list[int, int]]): A
        proposed solution of queen positions.

    Returns:
        bool: True if the candidate solution exists; otherwise False.
    """
    for existing_solution in solutions:
        if all(existing_solution[i] == candidate_solution[i]
                for i in range(n)):
            return True
    return False


def try_to_build_solution(row, current_solution):
    """
    Recursively attempts to build a solution by placing queens row by row.

    Args:
        row (int): The current row being evaluated for queen placement.
        current_solution (list[list[int, int]]):
        The list of queen positions so far.
    """
    if row == n:
        # Full solution found; check for uniqueness and add to solutions.
        if not solution_is_unique(current_solution):
            solutions.append(current_solution.copy())
    else:
        for col in range(n):
            pos = [row, col]
            if all(
                not queens_are_attacking(pos, placed_pos)
                for placed_pos in current_solution
            ):
                current_solution.append(pos)
                try_to_build_solution(row + 1, current_solution)
                current_solution.pop()


def find_all_n_queen_solutions():
    """
    Initializes the board and triggers the solution-building process.
    """
    try_to_build_solution(0, [])


# Main execution
if __name__ == "__main__":
    n = parse_and_validate_input()
    find_all_n_queen_solutions()
    for solution in solutions:
        print(solution)
