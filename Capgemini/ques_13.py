#. Search in a row wise and column wise sorted matrix
# You are given an 'N * N' matrix of integers where each row and each column is sorted in increasing order. 
# You are given a target integer 'X'.


# Find the position of 'X' in the matrix. If it exists then return the pair {i, j} where 'i' represents 
# the row and 'j' represents the column of the array, otherwise return {-1,-1}
# For example:
# If the given matrix is:
# [ [1, 2, 5],
#   [3, 4, 9],
#   [6, 7, 10]] 
# We have to find the position of 4. We will return {1,1} since A[1][1] = 4.

n=3
matrix = [ [1, 2, 5], 
      [3, 4, 9],
      [6, 7, 10] ] 

target = 3

def findpos(n, matrix, target):
    row = 0
    col = n-1
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return (row,col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return (-1. -1)

print(findpos(n, matrix, target))