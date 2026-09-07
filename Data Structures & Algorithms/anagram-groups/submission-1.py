class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagMap = defaultdict(list)

        for w in strs:
            count = [0] * 26
            
            for c in w:
                count[ord(c) - ord("a")] += 1
            
            anagMap[tuple(count)].append(w)

        return list(anagMap.values())