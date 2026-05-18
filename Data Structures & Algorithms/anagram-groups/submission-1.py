class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for e in strs:
            key = ''.join(sorted(e))
            res[key].append(e)
        
        return list(res.values())


