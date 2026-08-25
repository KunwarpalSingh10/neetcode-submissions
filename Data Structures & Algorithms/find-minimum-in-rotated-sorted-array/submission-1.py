class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                smallest = min(smallest, nums[l])
                break

            m = (l + r) // 2
            smallest = min(smallest, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return smallest

            



