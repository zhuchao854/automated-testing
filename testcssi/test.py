a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in a:
    for j in i:
        print(j)

c=[print(j) for i in a for j in i]



n = (i for i in range(4))
print(list(n))


