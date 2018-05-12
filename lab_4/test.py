list_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list_b = []

for i in range(len(list_a)):
    if i%2 != 1:
        list_b.append(list_a[i])

print(list_b)
