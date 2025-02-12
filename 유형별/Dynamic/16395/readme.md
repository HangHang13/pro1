# 파스칼의 삼각형

> ![img](https://d2gd6pc034wcta.cloudfront.net/tier/6.svg) 

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 256 MB      | 4437 | 2894 | 2573      | 67.427%   |

## 문제

파스칼의 삼각형은 이항계수를 삼각형 형태로 배열한 것인데, 블레즈 파스칼(1623-1662)을 따라 이름 붙여졌다.

단순한 형태로, 파스칼의 삼각형은 다음과 같은 방법으로 만들 수 있다.

1. N번째 행에는 N개의 수가 있다.
2. 첫 번째 행은 1이다.
3. 두 번째 행부터, 각 행의 양 끝의 값은 1이고, 나머지 수의 값은 바로 위 행의 인접한 두 수의 합이다.

예를 들어, n=3이면 3번째 행의 2번째 수는 위 행의 인접한 두 수 (1과 1)을 더해서 만든다. 

n=6일 때, 파스칼 삼각형의 6번째 행의 10은 5번째 행의 인접한 두 수(4와 6)을 더해서 구한다. 

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Pascal%27s_triangle_5.svg/540px-Pascal%27s_triangle_5.svg.png)

같은 방식으로 n=11일 때, 다음과 같은 파스칼의 삼각형을 만들 수 있다.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Pascal_triangle.svg/588px-Pascal_triangle.svg.png)

정수 n과 k가 주어졌을 때 파스칼의 삼각형에 있는 n번째 행에서 k번째 수를 출력하는 프로그램을 작성하시오.  이때, 이 수는 이항계수 C(n-1,k-1)임에 주의하시오.

## 입력

첫째 줄에 정수 n과 k가 빈칸을 사이에 두고 차례로 주어진다. 이 때, 1 ≤ k ≤ n ≤ 30을 만족한다.

## 출력

첫째 줄에 n번째 행에 있는 k번째 수를 출력한다.

## 예제 입력 1 복사

```
5 3
```

## 예제 출력 1 복사

```
6
```

## 예제 입력 2 복사

```
11 3
```

## 예제 출력 2 복사

```
45
```



## 풀이

```python
n,m = map(int, input().split())
lst = []
for a in range(n):
    lst.append([])
    lst[a].append(1)

    for j in range(1,a):
        lst[a].append(lst[a-1][j-1]+lst[a-1][j])

    if n!=0:
        lst[a].append(1)


print(lst[n-1][m-1])
```

```
dasd
```

