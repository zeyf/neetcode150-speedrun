class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            word_list = list(word)
            word_list.sort()
            word_sorted_string = "".join(word_list)

            if word_sorted_string not in anagram_map:
                anagram_map[word_sorted_string] = [word]
            else:
                anagram_map[word_sorted_string].append(word)
        
        return list(anagram_map.values())