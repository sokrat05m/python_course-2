def max_subarray(arr):
    if not arr:
        return 0

    max_sum = current_sum = 0

    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


