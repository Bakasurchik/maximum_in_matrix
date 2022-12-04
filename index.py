def filling_matrix(row):
    return [[int(elem) for elem in input().split()] for i in range(row)]

def maximum_in_matrix(matrix):
    largest = max([max(row) for row in matrix])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == largest:
                return [i, j]

def main():
    n = int(input())
    m = int(input())
    matrix = filling_matrix(n)

main()