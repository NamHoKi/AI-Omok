class Offset(object):
    def __init__(self):
        # 3시부터 시계방향 // 8방향
        self.offset = [[0, 1],
                       [1, 1],
                       [1, 0],
                       [1, -1],
                       [0, -1],
                       [-1, -1],
                       [-1, 0],
                       [-1, 1]
                       ]