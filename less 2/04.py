input_items = input("Перечень: ")
terms = input_items.split()
for count, term in enumerate(terms):
    print(f"#{count+1}-{term[:10]}")

