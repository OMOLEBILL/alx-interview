#!/usr/bin/python3
"""fewwest coin I can give change"""


def makeChange(coins, total):
    """"Let give some change """
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each total
    # amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
