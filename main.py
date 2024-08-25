def coin_exchange_rec(coinsList: list, change: int):
    r = [0] * (change + 1)
    return coin_exchange_aux(coinsList, change, r)


def coin_exchange_aux(coinsList: list, change: int, r: list) -> int:
    if change == 0:
        return 0
    
    if change in coinsList:
        return 1
    
    if r[change] > 0:
        return r[change]
    
    min_coins = change

    for coin in coinsList:
        if coin <= change:
            num_coins = 1 + coin_exchange_aux(coinsList, change - coin, r)
            if num_coins < min_coins:
                min_coins = num_coins
    
    r[change] = min_coins
    return min_coins
