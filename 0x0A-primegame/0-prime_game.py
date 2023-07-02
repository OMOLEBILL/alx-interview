#!/usr/bin/python3
"""We find the winner of the game """


def generate_primes(n):
    """we get generate_primes(n) to be a function of n"""
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    for p in range(int(n**0.5) + 1, n + 1):
        if sieve[p]:
            primes.append(p)

    return primes


def simulate_game(n):
    """ "we get simulate_game(n) to be a function of n"""
    primes = generate_primes(n)
    num_primes = len(primes)
    if num_primes % 2 == 0:
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
    """we get isWinner(x, nums) to be a function of x and n
    if x == "Ben":
        return nums[0]
    else:
        return nums[1]"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if simulate_game(n) == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
