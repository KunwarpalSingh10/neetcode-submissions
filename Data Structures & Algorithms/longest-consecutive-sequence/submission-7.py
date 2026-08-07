class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        setNums = set(nums)
        
        for n in nums:
            if (n-1) not in setNums:
                count = 0
                while (count + n) in setNums:
                    count += 1
                res = max(res, count)
        return res
