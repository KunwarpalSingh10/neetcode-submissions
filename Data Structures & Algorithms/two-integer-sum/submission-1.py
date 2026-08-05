class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Dont use the set because it does not return the indices
        #Main idea is to find the difference in the set from the target to current element
        l = []
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in hmap and i != hmap[target - nums[i]]:
                return [i, hmap[target - nums[i]]]
                