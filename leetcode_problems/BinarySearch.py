# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current_node = root
        if current_node == None or val == current_node.val:
            return current_node
        elif val < current_node.val:
            return self.searchBST(current_node.left, val)
        elif val > current_node.val:
            return self.searchBST(current_node.right, val)
        