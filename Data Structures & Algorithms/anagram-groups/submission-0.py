class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            seen[key].append(s)

        return list(seen.values())
