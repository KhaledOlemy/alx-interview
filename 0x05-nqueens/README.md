### The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: nqueens N
    - If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
    - If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    - If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module

3 | 3 4 5 6
2 | 2 3 4 5
1 | 1 2 3 4
0 | 0 1 2 3
--|----------
  | 0 1 2 3


[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

<!-- def solve_queens(n: int):
    """solve the n-queens problem"""
    main_board = [n*[0]]*n
    # board = main_board.copy()
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    starting_row = 0
    solved = solver(board, n, starting_row, [], [])
    print(solved)

        
def solver(main_board, n, current_row, solved_boards, used_cols):
    if current_row < n - 1:
        board = main_board.copy()
        for c in range(n):
            print(board)
            if current_row == 0:
                board[current_row][c] = 1
                used_cols.append(c)
                return solver(board, n, current_row+1, solved_boards, used_cols)
            elif c == 0:
                if board[current_row-1][c] != 1 and board[current_row-1][c+1] != 1 and c not in used_cols:
                    board[current_row][c] = 1
                    used_cols.append(c)
                    return solver(board, n, current_row+1, solved_boards, used_cols)
            elif c == n - 1:
                if board[current_row-1][c] != 1 and board[current_row-1][c-1] != 1 and c not in used_cols:
                    board[current_row][c] = 1
                    used_cols.append(c)
                    return solver(board, n, current_row+1, solved_boards, used_cols)
            else:
                if board[current_row-1][c] != 1 and board[current_row-1][c-1] != 1 and board[current_row-1][c+1] != 1 and c not in used_cols:
                    board[current_row][c] = 1
                    used_cols.append(c)
                    return solver(board, n, current_row+1, solved_boards, used_cols)
    if current_row == n - 1:
        for c in range(n):
            if c == 0:
                if board[current_row-1][c] != 1 and board[current_row-1][c+1] != 1 and c not in used_cols:
                    board[current_row][c] = 1
                    solved_boards.append(board)
                    return solver(board, n, current_row+1, solved_boards, used_cols)
            elif c == n - 1:
                if board[current_row-1][c] != 1 and board[current_row-1][c-1] != 1 and c not in used_cols:
                    board[current_row][c] = 1
                    solved_boards.append(board)
                    return solver(board, n, current_row+1, solved_boards, used_cols)
            else:
                if board[current_row-1][c] != 1 and board[current_row-1][c-1] != 1 and board[current_row-1][c+1] != 1 and c not in used_cols:
                    board[current_row][c] = 1
                    solved_boards.append(board)
                    return solver(board, n, current_row+1, solved_boards, used_cols)
    if current_row == n:
        return solved_boards -->


# def sumColumn(m, column):
#     total = 0
#     for row in range(len(m)):
#         total += m[row][column]
#     return total


# def checker(row_or_col):
#     if sum(row_or_col) % 1000000 > 1:
#         return False
#     return True


# def solve_queens(n: int):
#     """solve the n-queens problem"""
#     # main_board = [n*[0]]*n
#     # board = list(main_board)
#     # for row_index, row in enumerate(board):
#     #     for col_index, col in enumerate(board[row_index]):
#     #         ...
#     main_board = [0] * n * n
#     results = []
#     board = main_board.copy()
#     board = [0] * 16
#     indecies = {i: {} for i in range(n)}
#     for index in range(n):
#         indecies[index]["row_indecies"] = list(range(index*n, (index*n)+n))
#         indecies[index]["col_indecies"] = [index+(i*n) for i in range(n)]
        
    
            
# def assigner(main_board, n, indecies):
#     board = main_board.copy()
#     for i in board:
#         if i != 1 and i != 1_000_000:
#             status = checker