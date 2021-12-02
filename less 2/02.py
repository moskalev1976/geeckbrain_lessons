input_items = input('Перечень: ')
terms = input_items.split()
items_lenth = len(terms)
i=0
if items_lenth>1:
    while i<items_lenth-1:
        terms[i],terms[i+1] = terms[i+1], terms[i]
        i +=2
    print(terms)
    