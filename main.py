# Change Return Program
# Wallis

money = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]


def calculate_change(cost, payment):
    change = payment - cost
    return change


def calculate_coins(change):
    coins = []
    y = 0
    while True:
        if money[y] > change:
            y += 1
        elif money[y] < change:
            change = change - money[y]
            if y in range(0, 9):
                coins.append(int(money[y] / 100))
            else:
                coins.append(money[y] / 100)
        elif money[y] == change:
            coins.append(money[y] / 100)
            break
    print(coins)


print('---Change exchange program---')
print('----------By Wallis----------')

while True:
    cost = float(input('Enter a cost of a product: '))
    cost = int(cost * 100)
    payment = float(input('Enter how much client gave you: '))
    payment = int(payment * 100)
    change = calculate_change(cost, payment)
    calculate_coins(change)
    print('-' * 29)
