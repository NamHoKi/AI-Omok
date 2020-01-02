from Offset import Offset

class Rule(Offset):
    def __init__(self):
        super().__init__()

    def stone_check(self, x, y , board):
        '''
        원래 돌이 있는 자리인지, 좌표값 밖인지 체크합니다.

        :param x: int - 확인할 x좌표
        :param y: int - 확인할 y좌표
        :param board: Board - 오목판
        :return: bool - 둘 수 없으면 False, 둘 수 있으면 True
        '''
        if x < 0 or x >= len(board.omok_board) or y < 0 or y >= len(board.omok_board):
            return False
        elif board.omok_board[x][y] == 11 or board.omok_board[x][y] == 10:
            return False
        else:
            return True

    def three_x_three_check(self, x, y , board , color):
        '''
        3x3을 체크합니다.

        :param x: int - 확인할 x좌표
        :param y: int - 확인할 y좌표
        :param board: Board - 오목판
        :param color: int - 10 : 백 / 11 : 흑
        :return: bool - 3x3이면 False , 아니면 True
        '''
        b = board.omok_board
        o = self.offset
        three_count = 0
        three_way =  ['011100','001110','010110','011010'] # 3이 될수 있는 경우

        # 양방향으로 체크할것이기 때문에 for문은 4방향.
        for i in range(4):
            check_pattern = '1'
            x_check = x
            y_check = y
            for j in range(4):
                x_check += o[i][0]
                y_check += o[i][1]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                    break

                check_xy = b[x_check][y_check]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                        break
                if check_xy == color:
                    check_pattern = '1' + check_pattern
                elif check_xy < 10:
                    check_pattern = '0' + check_pattern
                else:
                    break
            x_check = x
            y_check = y
            for j in range(4):
                x_check -= o[i][0]
                y_check -= o[i][1]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                    break

                check_xy = b[x_check][y_check]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                        break
                if check_xy == color:
                    check_pattern = check_pattern + '1'
                elif check_xy < 10:
                    check_pattern = check_pattern + '0'
                else:
                    break

            for three_list in three_way:
                if three_list in check_pattern:
                    three_count+=1
                    break

        if three_count >= 2:
            return False

        return True

    def win_check(self, x, y , board, color):
        '''
        오목, 장목을 두었는지 확인하는 함수입니다.
        오목을 넘는 장목도 승리로 판단합니다.
        :param x: int - 방금 둔 수의 x좌표
        :param y: int - 방금 둔 수의 y좌표
        :param board: 오목 board
        :param color: int - 방금 둔 수의 색 10 : 백 , 11 : 흑
        :return: bool - True : 승리조건 만족 , False : 승리조건 불만족
        '''
        b = board.omok_board
        o = self.offset
        check_count = [1] * 8

        for i in range(8):
            x_check = x + o[i][0]
            y_check = y + o[i][1]
            while True:
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b) or b[x_check][y_check] != color:
                    break
                else:
                    if b[x_check][y_check] == color:
                        check_count[i] += 1
                        x_check = x_check + o[i][0]
                        y_check = y_check + o[i][1]
                    else:
                        break

        for i in range(4):
            if check_count[i] + check_count[i+4] -1 >= 5:
                return True

        return False