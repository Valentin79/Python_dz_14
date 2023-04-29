def add_matrix(self, other):
    """
    >>> add_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    >>> add_matrix([[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    Traceback (most recent call last):
    ...
    Exception: Количество строк и колонок матриц не совпадают
    """
    if (len(self[0])) != len(other) or (len(self)) != len(other):
        raise Exception("Количество строк и колонок матриц не совпадают")
    result = ([[self[i][j] + other[i][j] for j in range(len(self[0]))]
               for i in range(len(self))])
    return result


def mul_matrix(self, other):
    """
    >>> mul_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) 
    [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
    >>> mul_matrix([[1, 2, 3], [5, 6, 7]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[38, 44, 50, 56], [98, 116, 134, 152]]
    >>> mul_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3, 4], [5, 6, 7, 8]])
    Traceback (most recent call last):
    ...
    Exception: Количество строк и колонок матриц не совпадают
    """
    if (len(self[0])) != len(other):
        raise Exception("Количество строк и колонок матриц не совпадают")
    result = ([[sum([self[i][k] * other[k][j] for k in range(len(other))])
                for j in range(len(other[0]))] for i in range(len(self))])
    return result

def equals_matrix(self, other):
    """
    >>> equals_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> equals_matrix([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    """
    return self == other


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
