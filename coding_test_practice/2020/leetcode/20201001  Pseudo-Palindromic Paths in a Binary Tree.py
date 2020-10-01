# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt = 0
    def find(self, root:TreeNode, route:List, cnt:int) -> bool:
        #마지막 노드일때 지금까지 담은 경로를 확인한다. 이때 모든 요소가 짝수가 아니면 빈 배열을 return
        route = route^{root.val} #★☆○☆★ 가운데 하나빼고 다 짝수여야함 또는 그냥 다 짝수
        flag = False
        
        if root.left:
            self.find(root.left, route, cnt)
        if root.right:
            self.find(root.right, route, cnt)
        if not root.left and not root.right: #마지막이니 count
            if len(route)<2:
                self.cnt+=1
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        #find 함수돌려서 배열이 비어있지 않으면 counting
        stack = []
        
        self.find(root, set(), 0)
        return self.cnt
