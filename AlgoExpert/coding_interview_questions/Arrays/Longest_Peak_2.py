def longestPeak(array):
    # Write your code here.
    ans = 0
    n = len(array)
    for idx in range(n):
        i = j = idx
        while (i - 1 >= 0 and array[i-1] < array[i]) or (j + 1 < n and array[j] > array[j+1]):
            if i - 1 >= 0 and array[i-1] < array[i]:
                i -= 1

            if j + 1 < n and array[j] > array[j+1]:
                j += 1

        if i == idx or j == idx:
            continue
        ans = max(ans, j-i+1)

    return ans
