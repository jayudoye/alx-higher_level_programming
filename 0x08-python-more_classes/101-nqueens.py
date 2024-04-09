#!/usr/bin/python3
import sys

"""The N-Queens problem solution"""


class NQueensGeek:
    """N-Queen solution class"""
    def __init__(self, n):
        """initializer"""
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        """
        Check if it's safe to place a queen at board[row][col]
        """
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False

        return True

    def solve(self):
        """Solve the problem using backtracking and recursion"""
        def _solve(board, row):
            if row == self.n:
                self.solutions.append(board[:])  # Append a copy of the board
                return
            for col in range(self.n):
                if self.is_safe(board, row, col):
                    board[row] = col
                    _solve(board, row + 1)

        board = [-1] * self.n
        _solve(board, 0)

    def print_solutions(self):
        """Print all possible solutions in a matrix format"""
        for solution in self.solutions:
            positions = list(zip(range(n), solution))
            print(list(map(lambda x: list(x), positions)))


if __name__ == "__main__":
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

    solver = NQueensGeek(n)
    solver.solve()
    solver.print_solutions()
