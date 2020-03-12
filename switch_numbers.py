def switch(arr):
    for i in range(len(arr)-1):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
print(switch([1,2,3,4]))