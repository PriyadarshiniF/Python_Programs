def max_sum_subarray(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st = 0; en = 0; poi = 0
    for i in range(0, size):
        curr_sum = curr_sum + arr[i]

        if (max_so_far < curr_sum):
            max_so_far = curr_sum
            st = poi
            en = i
        if (curr_sum < 0):
            curr_sum = 0
            poi = i+1

    print("Maximum Subarray is", max_so_far)
    print("Start Index of Window", st)
    print("End Index of Window", en)

arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
max_sum_subarray(arr)

