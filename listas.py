def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


def numerospares(limit):
    a = 0
    while a <= limit:
        if a % 2 == 0:
            yield a
        a += 1


for num in numerospares(10):
    print(num)

# for num in fibonacci(10):
#    print(num)

