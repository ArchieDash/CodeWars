from collections import defaultdict


def tickets(people: list) -> str:
    cashbox = defaultdict(int)
    for ticket in people:
        if ticket == 25:
            cashbox[25] += 1
        elif ticket == 50:
            if cashbox[25] >= 1:
                cashbox[50] += 1
                cashbox[25] -= 1
            else:
                return 'NO'
        elif ticket == 100:
            if cashbox[50] >= 1 and cashbox[25] >= 1:
                cashbox[100] += 1
                cashbox[50] -= 1
                cashbox[25] -= 1
            elif cashbox[25] >= 3:
                cashbox[100] += 1
                cashbox[25] -= 3
            else:
                return 'NO'
    return 'YES'
