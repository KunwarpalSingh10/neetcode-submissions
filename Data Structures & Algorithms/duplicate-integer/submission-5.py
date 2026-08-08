class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = defaultdict(int)

        for _, n in enumerate(nums):
            hmap[n] += 1
        print(hmap)

        vals = hmap.values()

        if len(list(vals)) > 0 and max(list(vals)) > 1:
            return True
        return False
            