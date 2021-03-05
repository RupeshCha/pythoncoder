def binary_search(arr,target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        
        mid = (left + right)//2 
        print(mid)

        if ( arr[mid] == target):
            return mid
        elif (arr[mid]<= target):
            left = mid+1
        else:
            right = mid - 1
    return -1

res = binary_search([101,345,607,1011,1130],101)
if ( res == -1):
    print("target not found ")
else:
    print ("target al location {}".format(res))

