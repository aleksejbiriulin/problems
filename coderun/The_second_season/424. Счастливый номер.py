import sys

def min_n_s(n, s):
    if n * 9 < s:
        return []
    a = [0 for _ in range(n)]
    i = n - 1
    while i >= 0 and s > 0:
        if s <= 9:
            a[i] = s
        else:
            a[i] = 9
        s -= a[i]
        i -= 1
    return a

def next_s(a, s):
    s1 = sum(a)
    if s > s1 and s - s1 + a[-1] <= 9:
        a[-1] += s - s1
        return a
    for i in range(len(a) - 1, -1, -1):
        s1 -= a[i]
        # print(i, s, s1)
        if a[i] == 9:
            continue
        a[i] += 1
        x = a[i]
        j = len(a) - 1
        s2 = s - s1 - a[i]
        # print(i, s, s2, s1)
        if s2 < 0 or 9 * (len(a) - i) < s2:
            continue
        while j > i:
            if s2 <= 9:
                a[j] = s2
            else:
                a[j] = 9
            s2 -= a[j]
            # print(a[j], j, s2, i, s1, s)
            j -= 1
        a[i] += s2
        if a[i] <= 9:
            return a
    return []




def main():
    s = list(map(int, list(input())))
    n = len(s) // 2
    s1 = sum(s[:n])
    s2 = sum(s[n:])
    ans = next_s(s[n:], s1)
    if ans:
        s[n:] = ans
        return s
    if n * 9 != s1:
        x = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 9:
                s[i] = 0
                x = 1
            else:
                s[i] += 1
                break
        ans = min_n_s(n, sum(s[: n]))
        if ans:
            s[n:] = ans
            return s
    s = [0 for _ in range(n * 2)]
    s[n - 1] = 1
    s[2 * n - 1] = 1
    # print(5)
    return s
    

if __name__ == '__main__':
    print("".join(map(str, main())))