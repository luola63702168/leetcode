class Solution:

    def _chick(self, i):

        set_len_i = len(set(i))
        list_ = list()
        for j in range(9):
            if i[j] != ".":
                list_.append(i[j])
        return len(list_) != set_len_i - 1


    def _line(self):
        for section_list in self.board:
            if self._chick(section_list):
                continue
            else:
                return False
        return True

    def _rank(self):
        for i in range(9):
            screen_li = [self.board[j][i] for j in range(9)]
            if self._chick(screen_li):
                continue
            else:
                return False
        return True

    def _block(self):
        screen_li1, screen_li2, screen_li3 = [], [], []
        section_list = [(0, 3), (3, 6), (6, 9)]
        for t in section_list:
            for i in self.board[t[0]:t[1]]:
                screen_li1.extend(i[section_list[0][0]:section_list[0][1]])
                screen_li2.extend(i[section_list[1][0]:section_list[1][1]])
                screen_li3.extend(i[section_list[2][0]:section_list[2][1]])
            # print(screen_li1, screen_li2, screen_li3)
            if self._chick(screen_li1) and self._chick(screen_li2) and self._chick(screen_li3):
                screen_li1.clear()
                screen_li2.clear()
                screen_li3.clear()
                continue
            else:
                return False
        return True

    def isValidSudoku(self, board):
        '''
        这里的逻辑判断可以写为一行
        '''
        self.board = board
        # 测试每一行
        if not self._line():
            return False
        # 测试每一列
        elif not self._rank():
            return False
        # 测试每一小格
        elif not self._block():
            return False
        return True


if __name__ == '__main__':
    # false
    board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "6", ".", ".", ".", "."],
             ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
             [".", ".", ".", "7", ".", ".", ".", ".", "."],
             [".", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    # true
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    single = Solution()
    print(single.isValidSudoku(board))
