# ternary - single line conditional statement

print("A") if True else print("B")

n = 5
v = "it is 5" if n == 5 else "It is not 5"
print(v)

# lambda - single line shortcut function or anonymous function


def func1(num): return num ** 2


v1 = func1(4)
print(v1)

# lambda and map funciton together

ls1 = [1, 2, 3]
ls2 = list(map(lambda g: g ** 2, ls1))
print(ls2)
