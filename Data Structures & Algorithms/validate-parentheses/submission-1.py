class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        stack_map = {')' : '(', "}" : "{", "]" : "["}

        for c in s:
            if c in stack_map:
                top_element = stack.pop() if stack else "#"

                if stack_map[c] != top_element:
                    return False

            else: 
                stack.append(c) 

        return len(stack) == 0
            
            
            
        