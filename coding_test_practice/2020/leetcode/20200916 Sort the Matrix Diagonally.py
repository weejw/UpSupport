class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = {} # 부모 저장용 dic
        
        m, n = len(mat),len(mat[0])
        
        for i in range(-m+1, n): #양수,음수 key 생성
            dic[i] = []
        
        for row in range(m): #그림과 같이 탐색해서 부모를 찾아줌
            for col in range(n):
                dic[col-row].append(mat[row][col])
        
        for i in range(-m+1, n): #정렬
            dic[i] = sorted(dic[i])
        
        
        resmat = []
        for row in range(m): #정렬해서 저장한 부모에 있는 값을 하나씩 빼줌 
            newmat=[]
            for col in range(n):
                newmat.append(dic[col-row].pop(0))
            resmat.append(newmat)
            
        return resmat
