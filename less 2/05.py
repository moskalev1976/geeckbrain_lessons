range = [13,11,7,3,2,2,1,1,1]
ranging = int(input("Введите рейтинг: "))
input = False
for count, item in enumerate(range):
  if ranging > item:
    range.insert(count, ranging)
    input = True
    break
if not input:
  range.append(ranging)

print(range)
