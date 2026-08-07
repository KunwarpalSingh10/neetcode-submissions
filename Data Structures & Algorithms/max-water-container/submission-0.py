class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            small = min(heights[l],heights[r])
            current = small * (r - l)
            largest = max(current, largest)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return largest

        