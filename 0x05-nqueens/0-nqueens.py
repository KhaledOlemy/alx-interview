#!/usr/bin/python3
"""Solves the N Queens problem with backtracking."""
import sys


def fetch_board_size():
    """Fetches the board size from command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        return n
    except ValueError:
        print("N must be a number")
        sys.exit(1)


def can_attack(q1, q2):
    """Determines if two queens can attack each other."""
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])  # noqa


def check_unique(candidate, solutions):
    """Checks if a candidate solution is unique."""
    for sol in solutions:
        if set(map(tuple, candidate)) == set(map(tuple, sol)):
            return False
    return True


def solve_queens(row, positions, solutions, size):
    """Attempts to place queens on the board recursively."""
    if row == size:
        if check_unique(positions, solutions):
            solutions.append([p[:] for p in positions])
        return

    for col in range(size):
        new_pos = [row, col]
        if all(not can_attack(new_pos, p) for p in positions):
            positions.append(new_pos)
            solve_queens(row + 1, positions, solutions, size)
            positions.pop()


def n_queens(size):
    """Finds all solutions for the N queens problem of the given size."""
    solutions = []
    solve_queens(0, [], solutions, size)
    return solutions


if __name__ == "__main__":
    size = fetch_board_size()
    solutions = n_queens(size)
    for sol in solutions:
        print(sol)
