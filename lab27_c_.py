# a strung
word = "chandu yadav"
for letter in word :
    print(letter)

# using range to iterat from 0 to 4
for i in range(0,9):
    print(i)

# no of rows for the triangl
row = 6
for i in range(1,row +1):
    for j in range(i):
        print("*",end="")
    print()   

    # for loop with break 
    for i in range(11):
        if i == 6:
            break
        print(i)

# for loop with continue 
for i in range(10):
    if i % 2 == 0 :
        continue
    print(i) 

# for loop with eles 
for i in range(5):
    print(i)
else:
    print("its over")       