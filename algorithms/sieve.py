def sieve(max_prime=1000):
    """Returns an array of prime numbers up to the `max_prime`"""
    s = [True] * (max_prime+1)
    r = []
    for i in range(2, max_prime+1):
        if s[i]:
            r.append(i)
            for j in range(i*2, max_prime+1, i):
                s[j] = False
            return r


max_number = 1_000_000
numbers = sieve(max_number)
print(numbers)
print(f"Out of {max_number} numbers, {len(numbers)} are prime")
