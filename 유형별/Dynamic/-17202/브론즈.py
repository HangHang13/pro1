a=list(map(int, input()))
b=list(map(int, input()))

arr=[0]*16
for i in range(16):
    if i%2==0:
        arr[i] = a[i//2]
    else:
        arr[i] = b[i//2]



while len(arr) !=2:
    tmp=[]

    for i in range(len(arr)-1):
        num = (arr[i]+ arr[i+1])%10
        tmp.append(num)

    arr =tmp

print(*arr, sep="")