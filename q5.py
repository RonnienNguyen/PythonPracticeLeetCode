class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergeTwoLists(self, list1, list2):
        new = []
        for nums in list1:
            new.append(nums)
        for numss in list2:
            new.append(numss)
        result = sorted(new, reverse=False)
        return result
    def listToLinkedList(self, list1):
        if not list1:
            return None
        head = ListNode(list1[0])
        print(head.val)
        current = head
        for val in list1[1:]:
            current.next = ListNode(val)
            print(current.next.val)
            current = current.next
        return head
    
if __name__ == "__main__":
    
    solution = Solution()
    array1 = [1, 2, 4]
    array2 = [1, 3, 4]

    # result = solution.mergeTwoLists(array1, array2)
    # print(result)

    linked_list = solution.listToLinkedList(array1)
    print(linked_list)
    current = linked_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")