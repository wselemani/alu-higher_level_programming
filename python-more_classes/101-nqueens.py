#!/usr/bin/python3
"""N Queens problem - backtracking solution"""
import sys


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe"""
    for i in range(row):
        # Check same column
        if board[i] == col:
            return False
        # Check diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row, n, solutions):
    """Use backtracking to find all solutions"""
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n, solutions)
            board[row] = -1


def nqueens(n):
    """Main function to solve N queens"""
    board = [-1] * n
    solutions = []
    solve(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


# Validate arguments
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

nqueens(n)
