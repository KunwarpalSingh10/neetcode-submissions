class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            res[n] = i
        
        for i, n in enumerate(nums):
            if target - n in res and i != res[target - n]:
                return [i, res[target - n]] 