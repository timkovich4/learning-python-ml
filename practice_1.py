def count_coins(change):
    coins_5 = change // 5
    change = change % 5

    coins_2 = change // 2
    change = change % 2

    coins_1 = change // 1

    result = {
        "5_руб": coins_5,
        "2_руб": coins_2,
        "1_руб": coins_1
    }

    return result

print(count_coins(12))
print(count_coins(19))
print(count_coins(8))
