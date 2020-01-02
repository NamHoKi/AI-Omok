# -*- coding : utf-8 -*-
# python version : 3.7.3

from Board import Board
from Rule import Rule
from AI import AI

import random
import time
import sys
import pygame
from pygame.locals import *

class Main(object):
    def start(self):
        '''
        오목 게임을 시작하고 진행합니다.
        한 게임이 끝나면 5초 뒤 다시 새로운 게임이 시작됩니다.
        :return:
        '''
        board = Board()
        ai = AI('AI', '○')
        rule = Rule()
        turn = True  # AI 차례 : False , user 차례 : True
        count = 1

        pygame.init()

        screen = pygame.display.set_mode((800, 440))
        pygame.display.set_caption('오목')

        rand_x = random.randrange(8,12)
        rand_y = random.randrange(8,12)

        board.put_stone(rand_y,rand_x,11)

        rand_x = rand_x * 21 + 10
        rand_y = rand_y * 21 + 10

        black_stones = [[rand_x, rand_y]]
        white_stones = []

        end_check = False
        while True:
            user_select_x = False
            user_select_y = False
            three_x_three_warning = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                LEFT = 1  # 왼쪽 버튼에 대한 버튼 인덱스

                if event.type == MOUSEBUTTONUP and event.button == LEFT:
                    mouse_xy = pygame.mouse.get_pos()
                    x = (mouse_xy[0] - 10) // 21
                    y = (mouse_xy[1] - 10) // 21
                    user_select_x = y
                    user_select_y = x

                elif event.type == MOUSEMOTION:
                    mouse_xy = pygame.mouse.get_pos()
                    x = (mouse_xy[0] - 10) // 21
                    y = (mouse_xy[1] - 10) // 21
                    temp_x = x * 21 + 10
                    temp_y = y * 21 + 10


            # 게임의 상태를 업데이트하는 부분
            if turn == False:
                x, y = ai.select_stone(board)
                gui_x = y*21 + 10
                gui_y = x*21 + 10
                board.put_stone(x, y, 11)
                black_stones.append([gui_x,gui_y])
                if rule.win_check(x, y, board, 11):
                    end_check = 'black'
                count += 1
                turn = not turn
            else:
                if user_select_x and user_select_y:
                    x, y = user_select_x, user_select_y
                    gui_x = y * 21 + 10
                    gui_y = x * 21 + 10
                    if rule.stone_check(x, y, board):
                        if rule.three_x_three_check(x, y, board, 10):
                            white_stones.append([gui_x, gui_y])
                            board.put_stone(x, y, 10)
                            if rule.win_check(x, y, board, 10):
                                end_check = 'white'
                            count += 1
                            turn = not turn
                        else:
                            three_x_three_warning = True


            # 게임의 상태를 화면에 그려주는 부분 -> 화면을 지우고, 그리고, 업데이트하는 코드가 들어감
            screen.fill((255, 255, 255))
            screen.blit(pygame.image.load('Image/omok_board.jpg'), (0, 0))
            screen.blit(pygame.image.load('Image/rule.jpg'), (440,0))

            for st in white_stones:
                pygame.draw.circle(screen, (250, 250, 250), st, 10)

            for st in black_stones:
                pygame.draw.circle(screen, (0, 0, 0), st, 10)

            pygame.draw.circle(screen,(120,120,120),black_stones[-1],10)

            if three_x_three_warning:
                screen.blit(pygame.image.load('Image/33.jpg'),(200,100))
                pygame.display.update()
                time.sleep(1)

            if temp_x <= 420 and temp_y <= 420:
                pygame.draw.circle(screen, (220,220,220),[temp_x,temp_y],10)

            if end_check == 'black':
                for i in range(5,0,-1):
                    screen.blit(pygame.image.load('Image/ai'+str(i)+'.jpg'), (465, 55))
                    pygame.display.update()
                    time.sleep(1)
            elif end_check == 'white':
                for i in range(5,0,-1):
                    screen.blit(pygame.image.load('Image/user'+str(i)+'.jpg'),(465,55))
                    pygame.display.update()
                    time.sleep(1)
            else:
                pygame.display.update()

            if end_check:
                self.start()

main = Main()
main.start()