def f(arr):
    # Sprawdzamy czy suma każdego wiersza równa się sumie odpowiadającej kolumny
    for i in range(len(arr)):
        row_sum = sum(arr[i])
        col_sum = sum(arr[j][i] for j in range(len(arr)))
        if row_sum != col_sum:
            return False
    return True



if __name__ == "__main__":
    print(f([[3,7,2],
             [4,2,5],
             [5,2,1]]))
    
    print(f([[3,7,2],
             [4,2,5],
             [9,2,1]]))