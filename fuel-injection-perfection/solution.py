
def solution(n):
    n = int(n)
    count = 0

    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            a = n + 1
            b = n - 1

            counta = countb = 0

            while a % 2 == 0:
                a = a / 2
                counta += 1

            while b % 2 == 0:
                b = b / 2
                countb += 1

            if counta > countb and n != 3:
                n += 1
            else:
                n -= 1

        count += 1

    return count
