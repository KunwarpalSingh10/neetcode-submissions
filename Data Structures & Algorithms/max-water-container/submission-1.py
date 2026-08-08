class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        l = 0 
        r = len(heights) - 1
        while l < r:
            small = min(heights[l], heights[r])
            area = small * (r - l)
            biggest = max(biggest, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return biggest