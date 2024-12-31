exp =-1
total =0
maxexp = 0
minexp = float('inf')
while exp!=0:
    exp= int(input("What is the expense? (type 0 to stop)"))
    total=total+ exp
    if exp>maxexp:
        maxexp=exp
    if exp!=0:
        if exp<minexp :
            minexp=exp    
print("Your total expenditure is "+ str(total))
print("The maximum you spent is " + str(maxexp))
print("The minimum you spent is " + str(minexp))