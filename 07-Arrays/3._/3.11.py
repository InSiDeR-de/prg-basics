def bubble_sort(arr):
    i=0
    n = range(len(arr)-1,0,-1)

    for i in n:
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

if __name__ == '__main__':
    print(bubble_sort([34,7,19,4,21,8]))
    print(bubble_sort([15, 8, 31, 47, 2, 19]))
    print(bubble_sort([3,7,1,0,4]))