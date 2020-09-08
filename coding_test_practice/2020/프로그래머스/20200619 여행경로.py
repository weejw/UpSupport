import copy

candiDate = []
def dfs(city, tickets, route, routeL):
    currentRoute = copy.deepcopy(route)
    currentRoute.append(city)

    if len(currentRoute) == routeL:
        candiDate.append(currentRoute)
    elif city not in tickets:
        return
    else:

        for nextCity in tickets[city]:
            currentTickets = copy.deepcopy(tickets)
            currentTickets[city].remove(nextCity)
            dfs(nextCity, currentTickets, currentRoute, routeL)


def solution(tickets):
    answer = []
    routeL = len(tickets)+1

    dic = {}
    for k, v in tickets:
        if k in dic:
            dic[k].append(v)
        else:
            dic[k] = [v]

    dfs("ICN", dic, [], routeL)

    return sorted(candiDate)[0]
