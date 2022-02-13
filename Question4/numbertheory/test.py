def get_proper_divisors(N):
    divisors = [x for x in range(1, N) if N % x == 0]
    print(divisors)
    return divisors

get_proper_divisors(20)