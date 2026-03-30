# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indicies = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0

        return self.dfs(indicies, self.pre_idx, preorder, 0, len(inorder) - 1)
    
    def dfs(self, indicies, pre_idx, preorder, left, right):
        if left > right:
            return None
        
        root_val = preorder[self.pre_idx]
        self.pre_idx += 1
        
        root = TreeNode(root_val)
        mid = indicies[root_val]
        root.left = self.dfs(indicies, pre_idx, preorder, left, mid - 1)
        root.right = self.dfs(indicies, pre_idx, preorder, mid + 1, right)
        return root
        