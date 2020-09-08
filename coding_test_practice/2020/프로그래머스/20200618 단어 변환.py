import copy

minStep = 50
def dfs(currentWord, words, step, target):
    if currentWord != target:
        wordArr = copy.deepcopy(words)
        wordArr.remove(currentWord)
        step += 1
        for word in wordArr:
            compareWord = zip(currentWord, word)

            cnt = 0
            for twoWord in compareWord:
                if twoWord[0] != twoWord[1]:
                    cnt += 1
            if cnt == 1:
                dfs(word, wordArr, step, target)

    if currentWord == target:
        global minStep
        minStep = min(minStep, step)


def solution(begin, target, words):
    if target not in words:
        return 0

    for word in words:
        compareWord = zip(begin, word)

        cnt = 0
        for twoWord in compareWord:
            if twoWord[0] != twoWord[1]:
                cnt += 1

        if cnt == 1:
            dfs(word, words, 1, target)

    return minStep
