def compare(arr1, arr2):
    result=None
    if len(arr1)!=len(arr2):
        return False
    else:
        i=0
        while i<len(arr1):
            if arr1[i]==arr2[i]:
                result=True
            else:
                return False
            i+=1
        return result
            



if __name__ == "__main__":
    print(compare(["water","book","sky"],["water","book","sky"]))
    print(compare([True,False],[True,False,True]))
    print(compare([5,3,1],[3,5,1]))
    print(compare([3,2,1],[3,2]))