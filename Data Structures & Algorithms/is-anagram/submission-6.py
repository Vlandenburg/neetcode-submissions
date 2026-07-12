class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map={}
        t_map={}
        for i in s:
            s_map[i]=s_map.get(i,0)+1
        for p in t:
            t_map[p]=t_map.get(p,0)+1
        if s_map==t_map:
            return True
        else:
            return False