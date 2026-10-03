from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = defaultdict(list)
        ans = []

        dictt = {}

        # dictionary with count of the number {1:1,2:2,3:3}
        for num in nums:
            
            if num not in dictt:
                dictt[num] = 1
            else:
                dictt[num] += 1
        
        # {1:[1], 2:[2], 3:[3]}
        for num,count in dictt.items():
            res[count].append(num)

        # Reversing the dict:
        for i in range(len(nums),0,-1):
            if i in res:
                for item in res[i]:
                    ans.append(item)
                    if len(ans) == k:
                        return ans
        

        

        

        
        
        