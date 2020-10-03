def solution(a, b):
    monthsD = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["THU","FRI","SAT","SUN","MON","TUE","WED"] #1월1일이 금요일이므로 idx 1이 금요일이 되게 위치
    return days[(sum(monthsD[:a-1])+b)%7]
