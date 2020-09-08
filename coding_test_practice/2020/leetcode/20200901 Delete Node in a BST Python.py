class Solution:
    def delete(self, node: TreeNode, key: int)->TreeNode:
        if node is None:
            return None
        else:
            if node.val == key:
                #4가지
                if node.left and node.right: # 자식이 다있음 > 대체 노드 탐색
                    parent, child = node, node.right

                    while child.left:
                        parent, child = child, child.left
                        
                    child.left = node.left
                    print(child.left.val)
                    
                    if parent != node:
                        parent.left = child.right
                        child.right = node.right
                        
                    node = child
                    print(node.val)
                    
                elif node.left or node.right:   # 자식이 둘중 하나만 있음
                    node = node.left or  node.right
                    
                else: #자식이 없음
                    node = None
                    return node
                
            if node.val > key:
                node.left = self.delete(node.left, key)
            else:
                node.right = self.delete(node.right, key)
                
            return  node
                    
                
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        return self.delete(root, key)
