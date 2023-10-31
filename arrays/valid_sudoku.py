class Solution:

    def get_row(self, index: int) -> List[int]:
        return self.board[index]
    
    def get_col(self, index: int) -> List[int]:
        return [
            self.board[j][index]
            for j in range(len(self.board))
        ]
    
    def get_3_by_3(self, start_x: int, start_y: int) -> List[int]:
        result = []

        for x in range(start_x, start_x + 3):
            for y in range(start_y, start_y + 3):
                result.append(self.board[x][y])
        
        return result
    
    def has_duplicate_digits(self, sequence: List[str]) -> bool:
        digit_sequence = list(filter(lambda el: el != ".", sequence))
        return len(set(digit_sequence)) != len(digit_sequence)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board

        for x in range(9):
            if self.has_duplicate_digits(self.get_row(x)):
                return False
            
            if self.has_duplicate_digits(self.get_col(x)):
                return False
            
            if x % 3 == 0:
                for y in range(0, 9, 3):
                    if self.has_duplicate_digits(self.get_3_by_3(x, y)):
                        return False
        
        return True