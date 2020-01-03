## AI-Omok Mini Project
python version : 3.7
encoding : UTF-8
GUI : Pygame
------------
## ScreenShot
![omok](https://user-images.githubusercontent.com/48282708/71707199-feb57e00-2e2b-11ea-9257-977c33195025.png)
------------
## Rule
AI : 흑, User : 백
승리조건 : 5목 이상 (6목,, 7목 ... 등등)
3 x 3 : 흑,백 모두 금지
4 x 4 : 흑,백 모두 가능
시간제한 : 없음
------------
## Start
시작하면 흑(AI)이 먼저 돌을 놓습니다.
마우스로 백(User)이 놓을 곳을 선택합니다.
승리조건을 만족하면 5초 뒤 재시작합니다.
------------
## Memo
### 개선
1. 재시작 전 카운트 다운할 때, 마우스 이벤트 오류 수정
2. MinMax 알고리즘을 사용하여 더 많은 수 예측
