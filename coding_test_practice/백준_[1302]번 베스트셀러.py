dic={}
lis=[]
for _ in range(int(input())):
    bookName=input()

    if bookName in dic:
        dic[bookName]=dic[bookName]+1
    else:
        dic[bookName]=1

max_v=max(dic.values())

for book,num in dic.items():
    if num==max_v:
        lis.append(book)


result=sorted(lis)

print(result[0])
