#!/usr/bin/python3
import sys

"""
File solves nqueens
"""


class Queens:
    """Class Created to solve nqueens"""

    def __init__(self, n):
        """
        initiating instance with public attributes

        Args:
            - n: Number
        """
        self.n = n

    def print_solution(self, board) -> None:
        """Method used to print a solution"""
        for i in range(self.n):
            for j in range(self.n):
                print(board[i][j], end=" ")
            print()
        print()

    def is_safe(self, board: list, row: int, col: int) -> bool:
        """Method to check if safe to move queen"""
        # Check if there is a queen in the current row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower on the left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if board[i][j]:
                return False

        return True

    def helper(self, board, col) -> None:
        """Method acts as a helper recursive function"""
        # base case
        if col >= self.n:
            self.print_solution(board)
            return

        for i in range(self.n):
            if self.is_safe(board, i, col):
                # Place queen
                board[i][col] = 1

                self.helper(board, col+1)

                board[i][col]

    def solve(self) -> None:
        """Method used to Solve nqueen"""
        # intialize the board
        board: list = [
                [0 for _ in range(self.n)]
                for _ in range(self.n)
        ]
        self.helper(board, 0)


if __name__ == "__main__":

    arguments: list = sys.argv

    # Check the length of arguements should be exactly 2
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Grab the arguement
    N = sys.argv[1]

    # Check if N is an integer
    try:
        N: int = int(N)
    except Exception as e:
        print("N must be a number")
        sys.exit(1)

    # N must be greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens: Queens = Queens(N)
    nqueens.solve()
