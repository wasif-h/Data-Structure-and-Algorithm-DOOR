def even_odd(num):
    if (num % 2 == 0):
        return "Even"
    else:
        return "Odd"

# just like c++ we can choose argument and return type 
def func1(n1: int, n2: int) -> float:
    n3 = n1 + n2
    return n3

# default argument
def func2(n1, n2 = 40):
    n3 = n1 + n2
    return n3

# args 
def func3(*args):
    for arg in args:
        print(arg)
    
# **kwargs
def func4(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    


def main():
    num = 5
    print(even_odd(int(num)))
    
    print("Func1 = ",func1(3,6))
    print("Func2 = ",func2(3))
    print("Func3 = ")
    func3(3,31,56,74,23)
    print("Func4 = ")
    func4(home = 44,newtown = 5)
    


main()
