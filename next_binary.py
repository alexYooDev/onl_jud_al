def solution(n):

    bin = sum(list(map(int, str(format(n, 'b')))))

    for next_bin in range(n+1,1000000):
        if sum(list(map(int, str(format(next_bin, 'b'))))) == bin:
            break

    return next_bin