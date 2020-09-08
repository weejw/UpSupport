import re

str = '1D2S3T*'

p = re.compile('\d+[A-Z]\W?')

lst = p.findall(str)

for i in range(len(lst)):
    cal = lst[i]
    flag = -1

    if '#' in cal:
        cal = cal.replace("#","")
        flag = 0

    elif '*' in cal:
        cal = cal.replace("*", "")
        flag = 1

    cal = cal.replace("S", "**1")
    cal = cal.replace("D", "**2")
    cal = cal.replace("T", "**3")

    if flag == 0:
        cal += '*(-1)'

    elif flag == 1:
        cal += '*2'
        if i != 0:
            lst[i-1] += '*2'

    lst[i] = cal
    flag = -1

jCal="+".join(lst)
print(jCal)
print(eval(jCal))
