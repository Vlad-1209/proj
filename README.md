# proj
check_items = list()
check_items_prices = []
check = 0
check_sum = 0
check_number = 1


def add_item(item_name, item_cost):
    global check_items, check_sum, check
    check_items.append(item_name)
    check_items_prices.append(item_cost)
    check_sum += item_cost
    check += 1


def print_receipt():
    global check_items, check_sum, check_number, check, check_items_prices
    if bool(check_items):
        print(f"Чек {check_number}. Всего предметов: {check}")
        for i in range(len(check_items)):
            print(f"{check_items[i]} - {check_items_prices[i]}")
        print(f"Итого: {check_sum}")
        print('-----')
        check_items = []
        check_items_prices = []
        check = 0
        check_sum = 0
        check_number += 1

