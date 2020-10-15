one_quart = []
two_quart = []
three_quart = []
four_quart = []
new_number = 0

while new_number > -1:
    new_number = int(input("Adicione um novo número: "))
    if new_number > 0 and new_number <= 25:
        one_quart.append(new_number)
    elif new_number >= 26 and new_number <= 50:
        two_quart.append(new_number)
    elif new_number >= 51 and new_number <= 75:
        three_quart.append(new_number)
    elif new_number >= 76 and new_number <= 100:
        four_quart.append(new_number)
    print(f"0-25: {len(one_quart)}")
    print(f"26-50: {len(two_quart)}")
    print(f"51-75: {len(three_quart)}")
    print(f"76-100: {len(four_quart)}")
