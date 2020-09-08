################
# 2017. 6. 24. #
################

orgStick=64
count=0
want=int(input())

while(want!=0):
  if orgStick>want:
      orgStick=orgStick/2
  else:
      want=want-orgStick
      count=count+1

print(count)
