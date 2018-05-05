
def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


if __name__ == "__main__":

    num = 600851475143
    primes = primes_sieve(num)

    divisor = list()
    p = next(primes)
    while num != 1:
        if num%p == 0:
            num = num/p
            print(num,p)
            divisor.append(p)
        else:
            p = next(primes)

    print(divisor)


