import sys
from datetime import datetime


sys.setrecursionlimit(30000)


def coin_exchange_rec(coinsList: list, change: int):
    init_time = datetime.now()

    results = [0] * (change + 1)
    count_coin = coin_exchange_aux(coinsList, change, results)

    end_time = datetime.now()
    time_total = end_time - init_time

    return count_coin, time_total



def coin_exchange_aux(coinsList: list, change: int, results: list) -> int:
    if change == 0:
        return 0
    
    if change in coinsList:
        return 1
    
    if results[change] > 0:
        return results[change]
    
    min_coins = change

    for coin in coinsList:
        if coin <= change:
            num_coins = 1 + coin_exchange_aux(coinsList, change - coin, results)
            if num_coins < min_coins:
                min_coins = num_coins
    
    results[change] = min_coins
    return min_coins




def coin_exchange_iter(coinsList: list, change: int):
    init_time = datetime.now()
    if change == 0:
        return 0
    
    if change in coinsList:
        return 1

    results = [0] * (change + 1)

    for unit in range(change+1):
        num_coins = unit

        for coin in coinsList:
            if coin > unit:
                continue

            if 1 + results[unit - coin] < num_coins:
                num_coins = results[unit - coin] + 1
        results[unit] = num_coins
    
    end_time = datetime.now()
    
    time_total = end_time - init_time

    return results[change], time_total



def metrics_algorithms(coinlists: list, change: int):
    avg_iter = 0
    avg_rec = 0
    num_tests = 20

    for _ in range(num_tests):
        _, time_iter = coin_exchange_iter(coinlists, change)
        avg_iter += time_iter.total_seconds()

        _, time_rec = coin_exchange_rec(coinlists, change)
        avg_rec += time_rec.total_seconds()

    avg_iter /= num_tests
    avg_rec = avg_rec / num_tests

    print(f"Média de Tempo REC: {avg_rec} segundos\nMédia de Tempo ITER: {avg_iter} segundos")


coinlist = [1, 2, 5, 10, 50]
metrics_algorithms(coinlist, 15790)
