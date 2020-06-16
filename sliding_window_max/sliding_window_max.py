'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    output = [None] * (len(nums) - k + 1)
    # for i in range(0, len(nums)):
    #     for j in range(0, k):
    #         if i - j >= 0 and i - j < len(output):
    #             if output[i-j] is None:
    #                 output[i-j] = nums[i]
    #             elif output[i-j] < nums[i]:
    #                 output[i-j] = nums[i]

    temp = nums[0:k]
    temp_max = max(temp)

    for i in range(0, len(output)):
        output[i] = temp_max
        if i + k < len(nums):
            removed = temp.pop(0)
            temp.append(nums[i+k])
            if nums[i+k] > temp_max:
                temp_max = nums[i+k]
            elif removed == temp_max:
                temp_max = max(temp)

    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
