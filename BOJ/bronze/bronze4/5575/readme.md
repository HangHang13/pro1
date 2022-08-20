# 타임 카드 다국어한국어  

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 128 MB      | 4989 | 3779 | 3502      | 77.154%   |

## 문제

JOI 상사는 직원의 근무시간을 타임 카드로 관리하고있다. 직원들은 전용 장비를 사용하여 타임 카드에 출근 시간을 기록한다. 근무를 마치고 퇴근할 때도 타임 카드에 퇴근 시간을 기록한다. 타임카드에서 사용하는 시간단위는 24 시간제를 사용한다.

보안상의 이유로 직원들의 출근 시간은 7시 이후이다. 또한, 모든 직원은 23시 이전에 퇴근한다. 직원의 퇴근 시간은 항상 출근 시간보다 늦다.

입력으로 JOI 상사의 3 명의 직원 A 씨, B 씨, C 씨의 출근 시간과 퇴근 시간이 주어 졌을 때 각 직원의 근무시간을 계산하는 프로그램을 작성하라.

## 입력

입력은 3 행으로 구성된다.

첫 번째 줄에는 A 씨의 출근 시간과 퇴근 시간,

두 번째 줄에는 B 씨의 출근 시간과 퇴근 시간,

세 번째 줄에는 C 씨의 출근 시간과 퇴근 시간이 각각 공백으로 구분되어 있다.

시간은 각각 공백으로 구분된 3 개의 정수로 쓰여져있다.

3 개의 정수 h(7 ≦ h ≦ 22), m(0 ≦ m ≦ 59), s(0 ≦ s ≦ 59)는 h시 m 분 s 초를 나타낸다.

## 출력

첫 번째 줄에 A 씨의 근무 시간,

두 번째 줄에 B 씨의 근무 시간,

세 번째 줄에 C 씨의 근무 시간을 출력하라.

근무 시간이 h 시간 m 분 s 초이면 h, m, s의 순으로 공백으로 분리하여 출력하라.

## 예제 입력 1 복사

```
9 0 0 18 0 0
9 0 1 18 0 0
12 14 52 12 15 30
```

## 예제 출력 1 복사

```
9 0 0
8 59 59
0 0 38
```

## 풀이

```python

i=0
while i<3:
    a,b,c,d,e,f = map(int, input().split())
    a1=0
    a1+=a*60*60+b*60+c
    b1=0
    b1+=d*60*60+e*60+f
    k=b1-a1
    h=0
    m=0
    s=0
    h=k//3600
    m=(k%3600)//60
    s=(k%3600)%60

    print(h,m,s)
    i+=1
```

- 몫을 구해줬으면 되었을 문제인데.. int로 해버려서 이상해졌다.