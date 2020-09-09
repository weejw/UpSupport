class Solution:
    def dfs(self, res, node, total)-> List:
        if node.val == -1:
            return 
        
        res+=str(node.val)
        node.val = -1
        
        if not node.left and not node.right:
            exp, decimal = 0, 0
            for num in res[::-1]:
                decimal =+ decimal+int(num) * (2**exp)
                exp +=1
                
            total.append(decimal)
        
        if node.left:
            self.dfs(res, node.left, total)
        if node.right:
            self.dfs(res, node.right, total)
            
        return total
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return sum(self.dfs("", root, []))
