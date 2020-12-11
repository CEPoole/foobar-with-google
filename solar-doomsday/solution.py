import math


def solution(area):
    panels = []

    def loop(remaining):
        current = math.floor(math.sqrt(remaining))

        panel = int(current * current)
        panels.append(panel)

        new = remaining - panel

        if new != 0:
            loop(new)

    loop(area)
    return panels
