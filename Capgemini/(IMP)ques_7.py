#Calculate Spiral order matrix 



def spiral_order(matrix):
    result = []
    
    while matrix:
        # Step 1: Take the first row
        result += matrix.pop(0)
        
        # Step 2: Take the last element of each remaining row (right side)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        
        # Step 3: Take the last row in reverse
        if matrix:
            result += matrix.pop()[::-1]
        
        # Step 4: Take the first element of each remaining row in reverse (left side)
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(spiral_order(matrix))
