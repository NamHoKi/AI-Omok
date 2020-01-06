# AI-Omok Mini Project
------------
## Project info
##### - 오목판의 흐름을 스스로 판단하여 두는 AI를 만드는 것이 목표입니다.
##### - 학습이나 다음 수를 예상하는 것이 아닌 자신의 차례에서 가장 가치있는 곳에 돌을 둡니다.
##### - 오목판의 흐름을 판단할 때, 저의 주관적인 영향이 있을 수 있습니다.
## Cording
##### - python version : 3.7
##### - encoding : UTF-8
### Install
##### - GUI : Pygame
------------
## Rule
##### - AI : 흑, User : 백
##### - 승리조건 : 5목 이상 (6목,, 7목 ... 등등)
##### - 3 x 3 : 흑,백 모두 금지
##### - 4 x 4 : 흑,백 모두 가능
##### - 시간제한 : 없음
## Start
##### 1. 시작하면 흑(AI)이 먼저 돌을 놓습니다.
##### 2. 마우스로 백(User)이 놓을 곳을 선택합니다.
##### 3. 승리조건을 만족하면 5초 뒤 재시작합니다.

------------
## ScreenShot
![omok](https://user-images.githubusercontent.com/48282708/71707199-feb57e00-2e2b-11ea-9257-977c33195025.png)
------------
## Memo
### 개선
##### 1. 재시작 전 카운트 다운할 때, 마우스 이벤트 오류 수정
##### 2. MinMax 알고리즘을 사용하여 더 많은 수 예측
