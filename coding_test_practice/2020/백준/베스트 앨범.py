def solution(genres, plays):

    res = []
    totalL = list(zip(genres,plays))
    totalD = {} # 모든 장르별 랭킹
    eachD = {} # 장르내의 재생 횟수
    count = 0 # 고유번호 용

    

    for i in totalL:
        if i[0] in totalD:
            totalD[i[0]] += i[1]
            eachD[i[0]].append((count,i[1]))

        else:
            totalD[i[0]] = i[1]
            eachD[i[0]] = [(count,i[1])]

        

        count += 1

#장르별 전체 재생횟수 카운트 코드 끝

    totalD = sorted(totalD.items(), key = lambda x: x[1], reverse = True)
#전체 재생 횟수 sort 코드 끝



    for i in range(len(totalD)):
        totalD[i] = totalD[i][0]

# sorted 함수로 끝내고 싶었는데 안되서 꼼수 쓴 코드 끝 (언젠간 없에고말테야)



    for k, v in eachD.items():
        v.sort(key = lambda x: x[1], reverse = True)
        eachD[k]= v[:2]

# 2곡씩만 빼기위해서 슬라이스하고 장르별 음악 sort 코드 끝

    eachD = sorted(eachD.items(), key=lambda x: totalD.index(x[0]))
#전체 장르 기준으로 sort 코드 끝



    res = []
    for i in eachD:
        for j in i[1]:
            res.append(j[0])

    return res
