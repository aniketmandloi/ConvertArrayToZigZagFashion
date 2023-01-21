class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        flag = True
        for i in range(n - 1):
            if flag:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = not flag
