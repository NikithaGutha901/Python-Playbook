name = input("What is your Name?  ")
Age = int(input("what is your age  :"))

yearsto50= 50-Age

if yearsto50>0:
    print("Hello "+name+",You will be 50 in "+str(yearsto50)+"years")
else :
    print("Hello "+name+",You were 50 ago "+str(abs(yearsto50))+" years")
