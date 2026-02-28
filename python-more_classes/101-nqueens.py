#!/usr/bin/python3
"""
N Queens puzzle solver using Backtracking.
"""
import sys


def solve_nqueens(n):
    """
    Solves the N queens problem and returns all valid configurations.
    """
    cols = set()        # occupied columns
    pos_diag = set()    # occupied positive diagonals (row + col)
    neg_diag = set()    # occupied negative diagonals (row - col)
    
    board = []          # stores column index for each row
    res = []            # stores all valid solutions

    def backtrack(r):
        """
        Recursive backtracking function to place queens row by row.
        """
        # Əgər bütün sətirlərə (N) çata bildiksə, həlli tapdıq deməkdir
        if r == n:
            # Həlli tələb olunan [[r, c], ...] formatına salırıq
            formatted_solution = [[i, board[i]] for i in range(n)]
            res.append(formatted_solution)
            return

        for c in range(n):
            # Əgər sütun və ya diaqonallardan hər hansı biri doludursa, keç (continue)
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Kraliçanı yerləşdiririk və cədvəli yeniləyirik
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board.append(c)

            # Növbəti sətirə (r + 1) keçirik
            backtrack(r + 1)

            # Geriçəkilmə (Backtracking): Əgər bu yol işə yaramadısa,
            # qoyduğumuz kraliçanı geri götürürük və növbəti xananı yoxlayırıq.
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board.pop()

    # 0-cı sətirdən başlayırıq
    backtrack(0)
    return res


def main():
    """
    Main execution function for argument validation and running the solver.
    """
    # 1. Arqument sayını yoxla
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # 2. Arqumentin rəqəm (integer) olub-olmadığını yoxla
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # 3. Rəqəmin 4-dən böyük və ya bərabər olmasını yoxla
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Alqoritmi işə sal və hər həlli yeni sətirdə çap et
    solutions = solve_nqueens(n)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
