def get_matrix(n, m, value):
    # пустой список matrix
    matrix = []
    
    # первый(внешний) цикл for для кол-ва строк матрицы, n повторов.

    for _ in range(n):
        #  пустой список в список matrix
        row = []
        # второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
        for _ in range(m):
            # добавленный пустой список значениями value.
            row.append(value)
        # значение переменной matrix.
        matrix.append(row)
    
    #вернёт значение переменной matrix.
    return matrix

# Пример результата выполнения функции:
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)