a = 8 
b = 5.63
c = True
d = "Bangladesh"
e = 3 + 7j
e_func = complex(5,1)

print(a,b,c,d,e,e_func)
print(type(a),type(b),type(c),type(d),type(e))
print(id(a),id(b),id(c),id(d),id(e))

# swap

x = 6.3
y = 2
x,y = y,x
print(x,y)

# multiple assign
f = g = h = 50
print(f,g,h)


# typeCasting

j = int(b) # explicit
n1 = 5
n2 = 5.5
n3 = n1 + n2 #n1 implicitely converted to float
n4 = 5 + True # True converted to 1
print(j)
print(n3,type(n3),n4)

# float rounding 
v1 = 3.14164560736516596123987563985679134
v2 = round(v1,4)
print("Process 1 - ",v2)
print(f"Process 2 - {v1:.3f}")


# deleting varibale

del j