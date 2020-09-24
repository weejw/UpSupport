class Solution:
    def isValid(self, s: str) -> bool:
        #뚜껑과 그릇이 딱 만나는 순간에도 같아야한다
        stack = []
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            if char == ")" : #testcase ")"때문에
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            if char == "}" :
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            if char == "]" :
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        if stack: # testcase "["때문에
            return False
        return True
