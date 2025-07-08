# q3.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dumm = ListNode(0)
        current = dumm
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dumm.next

# Helper: convert list to linked list
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper: convert linked list to list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next

# Main logic to test the function
if __name__ == "__main__":
    l1 = list_to_linked_list([2, 4, 3])  # represents 342
    l2 = list_to_linked_list([5, 6, 4])  # represents 465
    print_linked_list(l1)
    print_linked_list(l2)
    solution = Solution()
    result_node = solution.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result_node)

    print("Result:", result_list)  # Output should be [7, 0, 8]
