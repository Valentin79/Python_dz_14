import pytest
from Matrix import add_matrix, mul_matrix, equals_matrix


@pytest.fixture()
def test_matrix_1():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.fixture()
def test_matrix_2():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.fixture()
def test_matrix_3():
    return [[1, 2], [4, 5]]


def test_add_matrix(test_matrix_1, test_matrix_2):
    assert add_matrix(test_matrix_1, test_matrix_2) == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]


def test_raises_add_matrix(test_matrix_1, test_matrix_3):
    with pytest.raises(Exception) as excinfo:
        add_matrix(test_matrix_1, test_matrix_3)
    assert "Количество строк и колонок матриц не совпадают" == str(excinfo.value)


def test_mul_matrix(test_matrix_1, test_matrix_2):
    assert mul_matrix(test_matrix_1, test_matrix_2) == [[30, 36, 42], [66, 81, 96], [102, 126, 150]]


def test_raises_mul_matrix(test_matrix_1, test_matrix_3):
    with pytest.raises(Exception) as excinfo:
        mul_matrix(test_matrix_1, test_matrix_3)
    assert "Количество строк и колонок матриц не совпадают" == str(excinfo.value)


def test_equals_matrix(test_matrix_1, test_matrix_2, test_matrix_3):
    assert equals_matrix(test_matrix_1, test_matrix_2) == True
    assert equals_matrix(test_matrix_1, test_matrix_3) == False

if __name__ == '__main__':
    pytest.main()