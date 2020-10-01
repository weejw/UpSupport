class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #정렬을 해놓고
        #두 수의 간격이 가장 작은거 = minimum absolute difference
        arr = sorted(arr)
        minNum = 10000000 #arr[i]가 10^6까지랬으니까
        dic = {} #작은 값들 저장할 dic
        
        for idx in range(len(arr)-1):
            tmp = abs(arr[idx]-arr[idx+1])
            if tmp <= minNum:
                minNum = tmp
                if tmp not in dic:
                    print(tmp)
                    dic[tmp] =[]
                dic[tmp].append([arr[idx],arr[idx+1]])

                               
        return dic[minNum]
