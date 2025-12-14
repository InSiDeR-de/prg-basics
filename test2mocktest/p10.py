



def f(array):
    # Find the minimum value in the 2D array
    min_val = float('inf')
    min_row = -1
    min_col = -1
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < min_val:
                min_val = array[i][j]
                min_row = i
                min_col = j
    
    # Check if row number equals column number (0-indexed)
    return min_row == min_col

if __name__ == "__main__":
    print(f([[7, 8], [5, 3], [9, 4]]))
    print(f([[7, 8, 5,3], [9, 4, 2, 6]]))