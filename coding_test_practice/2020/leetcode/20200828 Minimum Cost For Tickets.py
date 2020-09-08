class Solution:
    def mincostTickets(self, days, costs) :
        ticketCosts = [0 for i in range(max(days)+1)]

        def existIdx(paramDay): #-idx 에러 방지용
            try:
                return ticketCosts[paramDay]
            except IndexError:
                return 0
        # 오늘 사고 + 3 case
        # 1. 1일전에 티켓을 샀다.+
        # 2. 7일전에 티켓을 샀다.
        # 3. 30일전에 티켓을 샀다.

        for day in range(1, len(ticketCosts)):
            if day not in days:
                ticketCosts[day] = ticketCosts[day-1]
                continue

            print("현재 날짜:",day,
                  "\n1일전에 살경우:",existIdx(day-1)+costs[0],
                  "\n7일전에 살경우:",existIdx(day-7)+costs[1],
                  "\n30일전에 살경우:",existIdx(day-30)+costs[2])

            ticketCosts[day] = min(existIdx(day-1)+costs[0],
                                   existIdx(day-7)+costs[1],
                                   existIdx(day-30)+costs[2])

        return ticketCosts[-1]
