class ValFormatError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f"Error: Невозможно сложить матрицы, матрицы разных размеров"
        elif self.operation == '*':
            return f"Error: Невозможно перемножить матрицы: не подходят размерности"
        else:
            return f"Error: Невозможно сравнить. Матрицы разных размеров"