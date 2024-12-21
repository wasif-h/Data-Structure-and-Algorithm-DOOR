for i in range(2,20,5):
    print(i,"- Hello")
    
# if we don't need indexing then

for _ in range(2,20,5):
    print("Wall of Street")
    
# using two count together in for loop 

for i,j in zip([1,2,3],["a",'b','c']):
    print(i, j)
    
# Now make a pattern from for loop

for i in range(5):
    for j in range(5):
        print(j+1,end=" ")
    print()



