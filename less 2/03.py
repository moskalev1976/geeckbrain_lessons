month_count = input("Введите количество месяцев: ")
wi, sp, su, au = "зима", "весна", "лето", "осень"
months = {'1': wi, '2': wi, '3': sp, '4': sp, '5': sp, '6': su, '7': su, '8': su, '9': au, '10': au, '11': au, '12': wi}
print(months[month_count])
seasons = [wi, wi, sp, sp, sp, su, su, su, au, au, au, wi]
print(seasons[int(month_count)-1])
