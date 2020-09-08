################
# 2017. 6. 24. #
################

chess=[]
count=0
for _ in range(8):
   chess.append(input())

for y in range(8):
   if(y%2==0):    i=0
   else:  i=1
   for x in range(i,8,2):
      if chess[y][x] == 'F':
         count=count+1

print(count)
