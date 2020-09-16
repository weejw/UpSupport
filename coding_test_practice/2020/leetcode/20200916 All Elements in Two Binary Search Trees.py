# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, root, res):
        if root == "null":
            return
        res.append(root.val)
        root.val = "null"
        if root.left:
            self.search(root.left,res)
        if root.right:
            self.search(root.right,res)
        
        return res
        
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        if root1 is None:
            return sorted(self.search(root2,[]))
        if root2 is None:
            return sorted(self.search(root1,[]))
        
        res1 = self.search(root1,[])
        res2 = self.search(root2,[])
        
        return sorted(res1+res2)
