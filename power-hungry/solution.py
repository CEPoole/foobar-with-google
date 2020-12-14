import functools


def solution(xs):
    no_zeroes = filter(lambda x: x != 0, xs)
    answer = functools.reduce(lambda x, y: x * y, no_zeroes)

    if len(no_zeroes) != 1:
        answer = abs(answer)

    if answer < 0:
        remove = 1
        negatives = list(filter(lambda x: x < 0, xs))

        if len(negatives) > 1:
            remove = abs(max(negatives))

        answer = answer / remove

    return str(answer)
