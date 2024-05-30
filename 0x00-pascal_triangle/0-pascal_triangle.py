#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    output = []
    for i in range(1, n+1):
        line = [1]*i
        if i <= 2:
            output.append(line)
            continue
        prev = output[-1]
        for j in range(i):
            if j == 0 or list(range(i)).index(j) == list(range(i))[-1]:
                continue
            else:
                line[j] = prev[j] + prev[j - 1]
        output.append(line)
    return output

