import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone_weight for stone_weight in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest_stone, second_heaviest_stone = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)

            if heaviest_stone > second_heaviest_stone:
                heapq.heappush(
                    stones,
                    -1 * (heaviest_stone - second_heaviest_stone)
                )
        
        return 0 if len(stones) == 0 else -1 * stones.pop()