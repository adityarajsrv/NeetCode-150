class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in anagram_map:
                anagram_map[key] = []

            anagram_map[key].append(i)
        return list(anagram_map.values())