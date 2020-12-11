
def solution(l, t):
    for i in range(len(l) + 1):
        for j in range(i, len(l) + 1):
            if sum(l[i:j]) == t:
                return [i, j - 1]
    return [-1, -1]
