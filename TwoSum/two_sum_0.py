class Solution():
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
    
if __name__ == "__main__":
    solution = Solution()

    array = [1, 2, 3, 4]
    target = 3

    print(solution.twoSum(array, target))  # Output: [0, 1] or [1, 0] depending on the order of indices
    
