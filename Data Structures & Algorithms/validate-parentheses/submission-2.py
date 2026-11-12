class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        dict_validity = {
            '{':"}",
            '[':"]",
            '(':")"
        }
        for idx in range(1,len(s)) :
            if len(stack) != 0 : 
                temp = stack[-1]
                if temp in dict_validity and dict_validity[temp] == s[idx] : 
                    stack.pop()
                    continue
            stack.append(s[idx])
            
        return True if len(stack) == 0 else False