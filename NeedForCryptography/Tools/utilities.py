def det(matrix):
    '''
    Finds the determinant of a matrix.
    '''

    row_count = len(matrix)

    if row_count == 1:
        return matrix[0][0]

    return sum([((-1) ** i) * matrix[i][0] * det(minor(matrix, i + 1, 1))
                for i in range(row_count)])


def minor(matrix, row, column):
    '''
    Finds the minor of a matrix from the coordinates in the arguments.
    '''

    matrix_minor = matrix[:]
    del(matrix_minor[row - 1])
    matrix_minor = zip(*matrix_minor)
    del(matrix_minor[column - 1])
    return zip(*matrix_minor)
