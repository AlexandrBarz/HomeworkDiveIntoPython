# Напишите функцию для транспонирования матрицы

def matrix_transposition(matrix):
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return trans_matrix

matrix = [[5, 9, 16, 71],
          [6, 12, 10, 5]]

print("Исходная матрица:\n", matrix)
print(f"Транспонированная матрица:\n {matrix_transposition(matrix)}")