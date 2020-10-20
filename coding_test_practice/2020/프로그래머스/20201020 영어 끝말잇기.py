def solution(N, words):
    answer = []
    alreadyWord = [words[0]]
    
    prvWord = words[0]
    words = words[1:]
    for idx, word in enumerate(words,1):
        if prvWord[-1] != word[0] or word in alreadyWord:
            return [idx%N+1,idx//N+1]#누구차례라는건 idx%N으로 나눈것의 나머지 몇번째라는건 몫 idx//N
        alreadyWord.append(word)
        print(alreadyWord)
        prvWord = word
    return [0,0]
    # 1-N n명의 사람들
    # 1번부터 순서대로 단어를 말한다.(반복)
    # 영어로 끝말잇기(중복, 한글자 불가능)
    # n = 사람의 수 words = 말한 단어
    # 누가 가장먼저 ㅊ탈락하고 자신의 몇번째 차례에서 탈락하는지?
    # Counter로 2뜨는 단어 선택하고  = word
    # words 사람 수대로 잘라서 word 가지고 있는 사람 return
