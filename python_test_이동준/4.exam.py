i = 1
list_total = []

while i <= 10000:
    if (i % 3 == 0) or (i % 5 == 0):
        list_total.append(i)
    i = i + 1

with open('./python_test_이동준/result.txt', 'w', encoding='utf-8') as f:
    for line in list_total:
        f.write(str(line))
        f.write(' ')

