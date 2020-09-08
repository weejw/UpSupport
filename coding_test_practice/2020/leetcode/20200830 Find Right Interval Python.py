class Solution:
    def findNum(self, startPoints, endPoint):
        leftIdx = 0
        rightIdx = len(startPoints) - 1 # IndexError방지 -1
        resIdx = -1

        while leftIdx <= rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            if startPoints[midIdx][0] >= endPoint:
                rightIdx = midIdx - 1
                resIdx = startPoints[midIdx][1]
            else:
                leftIdx = midIdx + 1
        return resIdx

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startPoints = []
        endPoints = []
        for idx, num in enumerate(intervals):
            startPoints.append((num[0],idx))
            endPoints.append(num[1])

        startPoints = sorted(startPoints)  # 순서대로 입력이 들어온다는 말을 가정하지 않았음

        for idx, endPoint in enumerate(endPoints):
            endPoints[idx] = self.findNum(startPoints, endPoint)

        return endPoints
