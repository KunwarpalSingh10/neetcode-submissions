class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distances(x1, y1, x2, y2):
            return math.sqrt((x1-x2)**2 + (y1 - y2)**2)
        res = []
        heap = []
        for x, y in points:
            heapq.heappush(heap, (distances(x, y, 0, 0), x, y))

        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        
        return res

