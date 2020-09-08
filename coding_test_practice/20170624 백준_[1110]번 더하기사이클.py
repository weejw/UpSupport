input=int(input()) 
ten=orgTen=input//10 
one=orgOne=input%10 
cnt=0 
while True: 
    result=ten+one 
    ten=one%10 
    one=result%10 
    cnt=cnt+1 
    if cnt!=0 and ten==orgTen and one==orgOne: 
    break 
print(cnt)
