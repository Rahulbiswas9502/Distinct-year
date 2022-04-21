x=input("")
for i in range(9000) :

    x=int(x)
    x = x + 1
    x=x.__str__()
    a = (x[0])
    b = (x[1])
    c = (x[2])
    d = (x[3])
    if  a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
        break
    else:
       continue
print(x)

