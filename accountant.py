import sys

final_action = sys.argv[1:]
balance = 1000
warehouse = {}
logs = []

available_action = ["saldo", "zakup", "sprzedaz", "stop"]

while True:
    print("Dozwolone akcje: {}".format(", ".join(available_action)))
    action = input("Podaj rodzaj akcji: ")
    if action in available_action:
        if action == "stop":
            print("Koniec programu")
            break
        elif action == "saldo":
            balance_diff = int(input("Wprowadź kwotę: "))
            comment = input("Napisz komentarz: ")
            if balance + balance_diff < 0:
                print("Brak wystarczających środków. Aktualny stan konta: {}".format(balance))
                break
            balance += balance_diff
            logs.append([action, balance_diff, comment])
            print("-" * 50)
            print("Saldo: {}".format(balance))
            print("-" * 50)
        elif action == "zakup":
            product_id = input("Wprowadź identyfikator produktu: ")
            price = int(input("Wprowadź cenę jednostkową: "))
            qty = int(input("Wprowadź liczbę sztuk: "))
            if price < 0 or qty < 0:
                print("Błąd! Cena i ilość nie mogą mieć wartości ujemnej")
                break
            elif balance < price * qty:
                print("Brak wystarczających środków. Aktualny stan konta: {}".format(balance))
                continue
            elif product_id in warehouse:
                warehouse[product_id] += qty
            else:
                warehouse[product_id] = qty
            balance -= price * qty
            logs.append([action, product_id, price, qty])
            print("-" * 50)
            print("Saldo: {}".format(balance))
            print("Stan magazynowy: {}".format(warehouse))
            print("-" * 50)
        elif action == "sprzedaz":
            product_id = input("Wprowadź identyfikator produktu: ")
            price = int(input("Wprowadź cenę jednostkową: "))
            qty = int(input("Wprowadź liczbę sztuk: "))
            if price < 0 or qty < 0:
                print("Błąd! Cena i ilość nie mogą mieć wartości ujemnej")
                break
            elif warehouse.get(product_id, 0) < qty:
                print("Brak wystarczającej liczby produktów na magazynie")
                break
            balance += price * qty
            warehouse[product_id] -= qty
            logs.append([action, product_id, price, qty])
            print("-" * 50)
            print("Saldo: {}".format(balance))
            print("Stan magazynowy: {}".format(warehouse))
            print("-" * 50)
    else:
        print("Nieprawidłowa akcja! Dostępne: saldo, zakup, sprzedaż, stop")

# print("***Podsumowanie***")
# print(logs)
# print(warehouse)
# print("***Koniec podsumowania***")

if final_action[0] == "saldo":
    balance_diff = int(final_action[1])
    comment = final_action[2]
    if balance + balance_diff < 0:
        print("Brak wystarczających środków. Aktualny stan konta: {}".format(balance))
        exit()
    balance += balance_diff
    logs.append([action, balance_diff, comment])
    print("-" * 50)
    print("Saldo: {}".format(balance))
    print("-" * 50)
elif final_action[0] == "zakup":
    product_id = final_action[1]
    price = int(final_action[2])
    qty = int(final_action[3])
    if price < 0 or qty < 0:
        print("Błąd! Cena i ilość nie mogą mieć wartości ujemnej")
        exit()
    elif balance < price * qty:
        print("Brak wystarczających środków. Aktualny stan konta: {}".format(balance))
        exit()
    elif product_id in warehouse:
        warehouse[product_id] += qty
    else:
        warehouse[product_id] = qty
    balance -= price * qty
    logs.append([action, product_id, price, qty])
    print("-" * 50)
    print("Saldo: {}".format(balance))
    print("Stan magazynowy: {}".format(warehouse))
    print("-" * 50)
elif final_action[0] == "sprzedaz":
    if action == "sprzedaz":
        product_id = final_action[1]
        price = int(final_action[2])
        qty = int(final_action[3])
        if price < 0 or qty < 0:
            print("Błąd! Cena i ilość nie mogą mieć wartości ujemnej")
            exit()
        elif warehouse.get(product_id, 0) < qty:
            print("Brak wystarczającej liczby produktów na magazynie")
            exit()
        balance += price * qty
        warehouse[product_id] -= qty
        logs.append([action, product_id, price, qty])
        print("-" * 50)
        print("Saldo: {}".format(balance))
        print("Stan magazynowy: {}".format(warehouse))
        print("-" * 50)
elif final_action[0] == "konto":
    print("Stan konta: {}".format(balance))
    exit()
elif final_action[0] == "magazyn":
    for product in final_action[1:]:
        print("{}: {}".format(product, warehouse.get(product, 0)))
    exit()
elif final_action[0] == "przeglad":
    if len(final_action) < 3:
        print(logs)
        exit()
    idx_start = int(final_action[1]) - 1
    idx_end = int(final_action[2])
    print(logs[idx_start:idx_end])
    exit()

for action in final_action:
    print(action)
