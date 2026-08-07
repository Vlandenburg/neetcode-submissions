class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        sorted_a=dict(sorted(a.items(),key=lambda item:item[1],reverse=True))
        z = []
        return list(sorted_a.keys())[:k]



        