class Solution(object):
    def mergeTwoLists(self, list1, list2):
        new = []
        for nums in list1:
            new.append(nums)
        for numss in list2:
            new.append(numss)
        print(new)
        result = sorted(new, reverse=False)
        return result  
        
if __name__ == "__main__":

    solution = Solution()
    array1 = [1,2,4]
    array2 = [1,3,4]

    result = solution.mergeTwoLists(array1, array2)
    print(result)