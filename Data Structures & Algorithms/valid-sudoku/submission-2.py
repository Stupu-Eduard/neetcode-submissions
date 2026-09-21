class Solution:
    def validBox(self, box: List[int]) -> bool:
        line = [0] * 10
        for item in box:
            line[item] += 1
            if(line[item] > 1):
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check if the rows are valid
        for i in range(len(board)):
            line = [0] * 10
            for j in range(len(board[i])):
                val = board[i][j]
                if val != ".":
                    line[int(val)] += 1
                    if(line[int(val)] > 1):
                        return False
        
        # 2. Check if the columns are valid
        for j in range(len(board[0])):
            line = [0] * 10
            for i in range(len(board)):
                val = board[i][j]
                if val != ".":
                    line[int(val)] += 1
                    if(line[int(val)] > 1):
                        return False
        
        # 3. Check if the boxes are valid
        for m in range(3):
            for n in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        if board[m*3 + i][n*3 + j] != ".":
                            box.append(int(board[m*3 + i][n*3 + j]))
                if not self.validBox(box):
                    return False

        return True