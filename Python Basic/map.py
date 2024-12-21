# map -> modifying all element , accepting all element
ls1 = [1,2,3,4,5,6,7]

def func(n):
    return n*n

ls2 = list(map(func,ls1))
print("Map ls2 -:",ls2)
