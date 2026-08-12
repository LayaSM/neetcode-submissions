class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # psir [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: 
                # -1 will give the last element in the stack and since it is a list [0] will give us the first element of that list
                stack_t, stack_i = stack.pop() # directly assigning the items in the list respectively
                result[stack_i] = i - stack_i
            stack.append([t, i])
        
        return result


            
        