def filling_matrix(row):
    return [[int(elem) for elem in input().split()] for i in range(row)]

def main():
    n = int(input())
    m = int(input())
    matrix = filling_matrix(n)
    print(*matrix, sep='\n')

main()