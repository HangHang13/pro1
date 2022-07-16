# 😇1600 boj

# 말이 되고픈 원숭이

| 시간 제한 | 메모리 제한 | 제출  | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :--- | :-------- | :-------- |
| 2 초      | 256 MB      | 39929 | 8319 | 5133      | 18.775%   |

## 문제

동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 녀석은 말(Horse)이 되기를 간절히 원했다. 그래서 그는 말의 움직임을 유심히 살펴보고 그대로 따라 하기로 하였다. 말은 말이다. 말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다. 다음 그림에 말의 이동방법이 나타나있다. x표시한 곳으로 말이 갈 수 있다는 뜻이다. 참고로 말은 장애물을 뛰어넘을 수 있다.

|      | x    |      | x    |      |
| ---- | ---- | ---- | ---- | ---- |
| x    |      |      |      | x    |
|      |      | 말   |      |      |
| x    |      |      |      | x    |
|      | x    |      | x    |      |

근데 원숭이는 한 가지 착각하고 있는 것이 있다. 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다. 대각선 방향은 인접한 칸에 포함되지 않는다.

이제 원숭이는 머나먼 여행길을 떠난다. 격자판의 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다. 인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다. 격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수 K가 주어진다. 둘째 줄에 격자판의 가로길이 W, 세로길이 H가 주어진다. 그 다음 H줄에 걸쳐 W개의 숫자가 주어지는데, 0은 아무것도 없는 평지, 1은 장애물을 뜻한다. 장애물이 있는 곳으로는 이동할 수 없다. 시작점과 도착점은 항상 평지이다. W와 H는 1이상 200이하의 자연수이고, K는 0이상 30이하의 정수이다.

## 출력

첫째 줄에 원숭이의 동작수의 최솟값을 출력한다. 시작점에서 도착점까지 갈 수 없는 경우엔 -1을 출력한다.

## 예제 입력 1 복사

```
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
```

## 예제 출력 1 복사

```
4
```

## 예제 입력 2 복사

```
2
5 2
0 0 1 1 0
0 0 1 1 0
```

## 예제 출력 2 복사

```
-1
```







## 👺필요한 개념

- 리스트 순회

- 큰 값을 반환하는 if문 활용

## 👺풀이과정

- 올림 순열, 내림 순열을 각각 for문을 활용하여 검색
- 예를들어 리스트K[a]>=K[a-1]인 경우 카운트를 함
- 카운트 한 최대 횟수를 max_1 변수에 저장을 함
- 조건에 해당되지 않는 경우 카운트 변수를 1로 최기화함

## 👺코드


