class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        largest = 0

        for n in nums:
            if (n-1) not in numSet:
                count = 0
                while n + count in numSet:
                    count += 1
                largest = max(largest, count)
        return largest