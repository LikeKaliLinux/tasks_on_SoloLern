


#Option 1:

a = list(range(5,10,1))
for x in a:
    x = (input())
    if x == "op2":
        break
    a.append(x)
    del x
    print(a)


#Option 2:

a2 = list(range(1,6))
while True:
    x2 = (input())
    a2.append(x2)
    del x2
    print(a2)
