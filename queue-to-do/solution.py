import functools

def solution(start, length):
    acc = []

    sequence = range(start, start + length * length + 1)
    queues = [sequence[i:i + length] for i in range(0, len(sequence), length)]

    for x in range(0, len(queues)):
        q = queues[x]
        acc.extend(q[:length])
        length -= 1

    return functools.reduce(lambda a, b: a ^ b, acc)
