class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        max_area = 0

        while left < right: 
            area = min(heights[left], heights[right]) * (right-left)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

            max_area = max(max_area, area)

        return max_area



        