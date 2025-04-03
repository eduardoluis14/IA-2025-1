def print_board(board):
    for row in board:
        print(row)
    print()

def is_valid_2x2(board, row, col, num):
    # Verifica se o número pode ser colocado na posição (row, col)
    
    # Verifica linha e coluna
    for i in range(2):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # No 2x2, cada célula é seu próprio "sub-quadrado"
    return True

def is_valid_3x3(board, row, col, num):
    # Verifica se o número pode ser colocado na posição (row, col)
    
    # Verifica linha e coluna
    for i in range(3):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # Verifica o sub-quadrado 3x1
    subgrid_start = (col // 3) * 3  # No 3x3, isso sempre será 0, mas mantido para consistência
    for i in range(3):
        if board[row][i] == num:
            return False
    
    return True

def find_empty_location(board, size):
    # Encontra a próxima posição vazia (representada por 0)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board, size):
    # Encontra uma posição vazia
    empty = find_empty_location(board, size)
    
    # Se não há posições vazias, o sudoku está resolvido
    if not empty:
        return True
    
    row, col = empty
    
    # Tenta números de 1 a size
    for num in range(1, size+1):
        if size == 2:
            valid = is_valid_2x2(board, row, col, num)
        else:
            valid = is_valid_3x3(board, row, col, num)
        
        if valid:
            board[row][col] = num
            
            # Recursivamente tenta resolver o resto
            if solve_sudoku(board, size):
                return True
            
            # Se não der certo, backtrack
            board[row][col] = 0
    
    return False

def solve_sudoku_wrapper(board):
    size = len(board)
    
    print("Tabuleiro inicial:")
    print_board(board)
    
    if size not in [2, 3]:
        print("Tamanho de tabuleiro não suportado. Use 2x2 ou 3x3.")
        return
    
    if solve_sudoku(board, size):
        print("Solução encontrada:")
        print_board(board)
    else:
        print("Não há solução para este tabuleiro.")

# Exemplos de uso
print("=== Sudoku 2x2 ===")
sudoku_2x2 = [
    [1, 0],
    [0, 0]
]
solve_sudoku_wrapper(sudoku_2x2)

print("\n=== Sudoku 3x3 ===")
sudoku_3x3 = [
    [1, 0, 3],
    [3, 0, 1],
    [0, 3, 0]
]
solve_sudoku_wrapper(sudoku_3x3)

print("\n=== Sudoku 3x3 já resolvido ===")
sudoku_3x3_solved = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 3, 2]
]
solve_sudoku_wrapper(sudoku_3x3_solved)
