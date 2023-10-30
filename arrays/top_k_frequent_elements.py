from collections import Counter

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [f for f,s in list(sorted([(k,f) for k,f in Counter(nums).items()], key=lambda pair: pair[-1], reverse=True))][:k]
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [(value, frequency) for value, frequency in Counter(nums).items()]
        freq_list.sort(key=lambda value_frequency_pair: -value_frequency_pair[1])
        return [value for value, _ in freq_list][:k]