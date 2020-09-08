def timeFilter(time, bride_length):
    return time < bride_length + 1


def solution(bridge_length, weight, truck_weights):
    #어차피 트럭이 한대면 추가로 코드가 돌아갈 필요 없도록
    if len(truck_weights) == 1:
        return bridge_length + 1
    
    #변수 설정
    trucks = []
    bridge = []
    time = 0
    
    #(트럭무게, 시간)으로 데이터 변형
    for truck in truck_weights:
        trucks.append([truck, 0])
    
    #초기에 트럭 한대 미리 올려놓기
    bridge.append(trucks.pop(0))
    bridge[0][1] += 1
    time += 1
    
    #트럭 올릴까 말까 올릴까 말까 올릴까 말까 검사해서 올리기
    while trucks:
        totalWeight = sum([truck[0] for truck in bridge])
        if trucks[0][0] + totalWeight <= weight:
            bridge.append(trucks.pop(0))
        
        #올라가있는 트럭 객체의 시간 값 올려주기
        for truck in bridge:
            truck[1] += 1
        
        #내려가야할 트럭 검사
        bridge = list(filter(lambda truck:truck[1]<bridge_length,bridge))
        time += 1

    #트럭이 다 올라간 경우 마지막으로 올라간 트럭은 지나가야하니까 다리길이만큼 더해줌
    time += bridge_length 

    return time
