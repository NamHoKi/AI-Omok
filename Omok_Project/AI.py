from Offset import Offset

class AI(Offset):
    def __init__(self, nick_name,color):
        '''

        :param nick_name: string
        :param color: string
        '''
        super().__init__()
        self.nick_name = nick_name
        self.color = color

    def select_stone(self,board):
        '''
        self.AI_select_stone 을 호출하고 반환합니다.
        :param board: Board - 오목판
        :return: list - 최선의 수라고 판단 된 (x,y)좌표
        '''
        return self.AI_select_stone(board)

    def AI_select_stone(self,board):
        '''
        AI가 모든 좌표의 가중치 값중 가장 높은 값을 선택합니다.
        :param board: Board - 오목판
        :return: list - 최선의 수라고 판단 된 (x,y)좌표
        '''
        ai_max_weight = 0
        user_max_weight = 0
        max_weight = 0

        for i in range(20):
            for j in range(20):
                ai_weight = self.analysis_pattern(i,j,board,11)
                user_weight = self.analysis_pattern(i,j,board,10)

                if ai_weight >= 10000:
                    return i,j
                elif user_weight >= 10000 and ai_weight != -1:
                    user_weight = 10000

                if max_weight < ai_weight + user_weight and ai_weight != -1:
                    max_weight = ai_weight + user_weight
                    max_xy = [i,j]

                if ai_max_weight < ai_weight and ai_weight != -1:
                    ai_max_weight = ai_weight
                    ai_xy = [i,j]

                if user_max_weight < user_weight:
                    user_max_weight = user_weight

        if ai_max_weight >= user_max_weight:
            return ai_xy
        else:
            return max_xy

    def analysis_pattern(self, x, y , board , color):
        '''
        오목판의 (x,y)좌표의 가중치를 계산하여 반환합니다.
        :param x: int - x좌표
        :param y: int - y좌표
        :param board: Board - 오목판
        :param color: int - 10 : 백 / 11 : 흑
        :return: int - 가중치
        '''
        b = board.omok_board
        o = self.offset

        if b[x][y] >= 10:
            return -1

        two_1 = ['001010','010100','010010']
        two_2 = ['01100', '00110']
        three_6 = ['010110', '011010']
        three_8 = '01110'
        four_8 = ['10111','11011','11101']
        four_10 = ['11110','01111']
        four_50 =  '011110'

        weight = 0
        three_count = 0
        four_count = 0

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

            for three in three_6:
                if three in check_pattern and (not ('11101' in check_pattern)) and (not ('10111' in check_pattern)):
                    weight += 6
                    three_count += 1
                    if three_count == 2:
                        return -1

            if three_8 in check_pattern and (not ('11101' in check_pattern)) and (not ('10111' in check_pattern)):
                weight += 8
                three_count += 1
                if three_count == 2:
                    return -1

            if '11111' in check_pattern:
                return 10000

            if four_50 in check_pattern:
                weight += 50

            for two in two_1:
                if two in check_pattern:
                    weight += 1

            for two in two_2:
                if two in check_pattern:
                    weight += 2

            for four in four_8:
                if four in check_pattern:
                    weight += 8
                    four_count += 1
                    if four_count + three_count > 1:
                        weight += 150

            for four in four_10:
                if four in check_pattern:
                    weight += 10
                    four_count += 1
                    if four_count + three_count > 1:
                        weight += 150

        return weight