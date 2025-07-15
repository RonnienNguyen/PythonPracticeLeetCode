# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def height(self, root):
        if not root:
            return 0
        left_height = self.height(root.left)
        # print(left_height)
        right_height = self.height(root.right)
        # print(right_height)
        return max(left_height, right_height) + 1
    def convertToList(self, root):
        if not root:
            return []
        return self.convertToList(root.left) + [root.val] + self.convertToList(root.right)
    def convertFromList(self, lst):
        if not lst:
            return None
        mid = len(lst) // 2
        root = TreeNode(lst[mid])
        root.left = self.convertFromList(lst[:mid])
        root.right = self.convertFromList(lst[mid + 1:])
        return root


# Example usage:
if __name__ == "__main__":
    # Create a balanced binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    listNode = [1, 2, 3, 4, 5]

    # Check if the tree is balanced
    solution = Solution()
    # print(solution.height(root))  # Output: 3
    print(solution.convertToList(root))  # Output: [4, 2, 5, 1, 3]
    # print(solution.isBalanced(root))  # Output: True
    print(solution.convertFromList(listNode))  # Output: TreeNode with value 3
    # Create an unbalanced binary tree
    root_unbalanced = TreeNode(1)
    root_unbalanced.left = TreeNode(2)
    root_unbalanced.left.left = TreeNode(3)

    # Check if the unbalanced tree is balanced
    # print(solution.isBalanced(root_unbalanced))  # Output: False
            
            
        