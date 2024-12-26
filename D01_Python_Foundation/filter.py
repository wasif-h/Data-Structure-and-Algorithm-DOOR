# filter - accepting elements based on condition
ls1 = [1, 2, 3, 4, 5, 6]


def func(n):
    if (n % 2 == 0):
        return n

ls2 = list(filter(func,ls1))
print("Even-> ",ls2)
