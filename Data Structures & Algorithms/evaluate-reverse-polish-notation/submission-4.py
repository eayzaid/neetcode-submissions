from collections import deque
class Solution:

    def evaluate(self, a : int ,b : int, operation : str) : 
        if operation == '*' : 
            return a * b
        if operation == '/' :
            return int(b / a)
        if operation == '+' : 
            return a + b
        if operation == '-' : 
            return b - a
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for idx in range(len(tokens)) : 
            if tokens[idx] in ("+","-","*","/") : 
                a = int(stack.pop())
                b = int(stack.pop())
                res = str(self.evaluate(a,b,tokens[idx]))
                stack.append(res)
            else : 
                stack.append(tokens[idx])
        return int(stack.pop())