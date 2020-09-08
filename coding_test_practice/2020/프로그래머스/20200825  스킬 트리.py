def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        skill_tree = "".join(c for c in skill_trees[i] if c in skill)
        if len(skill_tree) == 0:
            answer += 1
            continue
        if len(skill_tree) < len(skill):
            for j in range(len(skill_tree)):
                if skill[j] != skill_tree[j]:
                    break
                if j == len(skill_tree)-1:
                    answer += 1
        else:
            for j in range(len(skill)):
                if skill[j] != skill_tree[j]:
                    break
                if j == len(skill)-1:
                    answer += 1

    return answer
