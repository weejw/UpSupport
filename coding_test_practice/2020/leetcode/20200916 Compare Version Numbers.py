#단순히 split()만 이용해서 자릿수 맞춰서 풀이함 40 ms	13.8 MB

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split("."), version2.split(".")

        if version1 == version2:
            return 0
        
        len1 , len2 = len(version1), len(version2)
        
        if len1 > len2:
            l = len1 - len2
            version2.extend([0]*l)
        elif len1 < len2:
            l = len2 - len1
            version1.extend([0]*l)
        
        for idx in range(len(version1)):
            if int(version1[idx]) > int(version2[idx]):
                return 1
            if int(version1[idx]) < int(version2[idx]):
                return -1
        return 0
       
       
#정규표현 사용
 import re

class Solution:
    def cmp(self, a, b):
        # False - False or True - True = 0
        # True - False = 1
        # False - True = -1
        return (a > b) - (a < b) 

    def compareVersion(self, version1: str, version2: str) -> int:
        # step1 : .0 제거
            # $  : 로 끝나는  것 ( 패턴 종료를 알림)
            # +  : 하나 이상 반복
            # () : 소괄호 안의 문자를 하나의 문자로 인식
            # *  : 앞문자가 있을수도 없을 수도
            # [] : 존재함
        
        pattern = '([.]0+)*$'
        version1 = re.sub(pattern,'', version1)
        version2 = re.sub(pattern,'', version2)
        
        
        # step2 : "dot(.)" 단위로 split()
        # 비교를 위해 dot(.) 단위로 split
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        
        # step3: 001 같은 값을 001 -> 1로 바꿔주기 위해 int()
        version1 = [int(i) for i in version1]
        version2 = [int(i) for i in version2]
        
        # 비교
        return self.cmp(version1, version2)
