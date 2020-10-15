n = int(input())
arr = list(range(1,n+1))
for i in range(3,n):
    arr[i] = (arr[i-1]+arr[i-2])%15746
print(arr[-1])

#토막상식 15746을 나누는 이유는 위에 점화식이 피보와 같은데 피보는 46번째 수가 2971215073가 되어 int의 범위를 초과해서 나누어주어야한다.
