import collections
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = collections.deque(stones)
        while len(q) > 1:
            s1 = max(q)
            q.remove(s1)

            s2 = max(q)
            q.remove(s2)

            if s1 < s2:
                q.append(s2 - s1)
            if s2 < s1:
                q.append(s1 - s2)
        return 0 if len(q) == 0 else q[0]
        

                