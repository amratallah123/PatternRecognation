x = 10

for i in range(1, 1000000):
    x = x - 0.001 * 2*(x-2)


print(x)
