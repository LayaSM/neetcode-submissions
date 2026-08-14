class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # s = d/t
        pair = [[pos, spd] for pos, spd in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[:: -1]:
            time = (target - p)/ s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
         
