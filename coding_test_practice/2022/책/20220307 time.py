import datetime
from datetime import timedelta

initial = timedelta(hours=0, minutes=0, seconds=0)
second_time = timedelta(hours=int(input()), minutes=59, seconds=59)

cnt = 0
while initial < second_time:
    initial += timedelta(seconds=1)
    if "3" in str(initial):
        cnt += 1
print(cnt)

# 책에서는.. 문자열로 진행했다.
