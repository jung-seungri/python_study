# 방코스 8월 2주차 10870번

n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    fibo = {}
    fibo[0] = 0
    fibo[1] = 1
    for i in range(n-1):
        fibo[i+2] = fibo[i] + fibo[i+1]
    print(fibo[n])