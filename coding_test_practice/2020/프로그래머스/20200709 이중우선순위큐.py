def solution(operations):
    heap = []
    for operation in operations:

        if operation[0] == "I":
            heap.append(int(operation[2:]))
        else:
            if heap:
                if operation[2] == "-":
                    heap.remove(min(heap))
                else:
                    heap.remove(max(heap))
    if not heap:
        return [0,0]
    return [max(heap), min(heap)]
