# A
list_1 = [57.8, 46.51, 97, 134.44, 145, 54, 44.55, 25.34, 334, 1987.5]
for prices in list_1:
    rub = int(prices)
    kk = (prices - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

# )  разделить срочки задач чтоб правельно отображалось
print(" ")
# B
list_1 = [57.8, 46.51, 97, 134.44, 145, 54, 44.55, 25.34, 334, 1987.5]
print(id(list_1))
list_1.sort()
print(id(list_1))
for prices in list_1:
    rub = int(prices)
    kk = (prices - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')

# )  разделить срочки задач чтоб правельно отображалось
print(" ")
# C
list_1 = [57.8, 46.51, 97, 134.44, 145, 54, 44.55, 25.34, 334, 1987.5]
for prices in sorted(list_1)[::1][:5]:
    rub = int(prices)
    kk = (prices - # )  разделить срочки задач чтоб правельно отображалось
print(" ")int(prices)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')

# )  разделить срочки задач чтоб правельно отображалось
print(" ")
# D
print([f'{int(prices)} руб {(prices - int(prices)) * 100:02.0f} коп' for prices in sorted(list_1)[::-1][:5]])
