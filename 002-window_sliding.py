def maxSum(arr, windowSize):
    arrSize = len(arr)
    max_sum = 0
    window_sum = 0

    if (arrSize < windowSize):
        return "please check input"
    window_sum = sum([arr[i] for i in range(windowSize)])

    for i in range(arrSize - windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]
        max_sum = max(max_sum, window_sum)
    return max_sum


arr = [1, 2, 100, 107, 5]
# maximum sum should be 104 => 100 + -1 + 5
answer = maxSum(arr, 3)
print(answer)