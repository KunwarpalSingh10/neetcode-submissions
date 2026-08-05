class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        count = 0
        for i in nums:
            res[i] += 1

        for _ in list(res):
            if len(res) != k:
                minkey = min(res, key = res.get)
                del res[minkey]
            else:
                break
        return list(res.keys())
        
        
            
