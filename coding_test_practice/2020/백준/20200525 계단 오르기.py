rN = int(input())

stairsN=[]

for _ in range(rN):
    stairsN.append(int(input()))


if rN == 1 or rN == 2:
    print(sum(stairsN))

else:
    maxVal = [stairsN[0],
          max(stairsN[0], stairsN[0] + stairsN[1]),
          max(stairsN[0] + stairsN[2], stairsN[1] + stairsN[2])
          ]

    for i in range(3, len(stairsN)):
        firstVal = maxVal[i-2] + stairsN[i]
        secondVal = maxVal[i-3] + stairsN[i] + stairsN[i-1]

        maxVal.append(max(firstVal, secondVal))

    print(maxVal[rN-1])
