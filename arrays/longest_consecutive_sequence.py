'''
class UnionFind:
    def __init__(self, n: int):
        self.__sets, self.__ranks, self.__max_rank = {}, {}, int(n > 0)
    
    def part_of_a_set(self, node: int) -> bool:
        return node in self.__sets
    
    def make_set(self, node: int) -> None:
        self.__sets[node], self.__ranks[node] = node, 1

    def find(self, node: int) -> int:
        if node == self.__sets[node]:
            return node
        
        self.__sets[node] = self.find(self.__sets[node])
        return self.__sets[node]
    
    def union(self, node_u: int, node_v: int) -> bool:
        u_set, v_set = self.find(node_u), self.find(node_v)

        if u_set == v_set:
            return False
        
        if self.__ranks[u_set] < self.__ranks[v_set]:
            self.__ranks[v_set] += self.__ranks[u_set]
            self.__ranks[u_set] = 0
            self.__sets[u_set] = v_set
        else:
            self.__ranks[u_set] += self.__ranks[v_set]
            self.__ranks[v_set] = 0
            self.__sets[v_set] = u_set

        self.__max_rank = max(
            self.__max_rank,
            self.__ranks[u_set],
            self.__ranks[v_set]
        )

        return True
    
    def get_max_rank(self) -> int:
        return self.__max_rank


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        union_find = UnionFind(len(nums))

        for num in nums:
            if not union_find.part_of_a_set(num):
                union_find.make_set(num)
            
            if union_find.part_of_a_set(num - 1):
                union_find.union(num - 1, num)
            
            if union_find.part_of_a_set(num + 1):
                union_find.union(num, num + 1)

        return union_find.get_max_rank()
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        ans = 0
        for num in nums:
            if num - 1 not in nums_set:
                current_sequence_length = 0
                while num + current_sequence_length in nums_set:
                    current_sequence_length += 1
            
                ans = max(ans, current_sequence_length)
        
        return ans
                
