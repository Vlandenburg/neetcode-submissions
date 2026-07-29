class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count = {}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word not in char_count:
                char_count[sorted_word]=[]
            char_count[sorted_word].append(word)
        return list(char_count.values())