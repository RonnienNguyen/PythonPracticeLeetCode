class Solution():
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == "__main__":
    solution = Solution()

    array = [1,2,3,4]
    target = 3

    print(solution.twoSum(array, target))

