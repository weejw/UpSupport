# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(X, Y, D):
    #개구리가 D만큼 음직일 수 있을때 Y+?*D = Y 이때 ?를 구하시오.
    #올림((Y-X )/D)
    return  math.ceil((Y-X)/D)
