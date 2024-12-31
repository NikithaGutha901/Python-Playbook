exp = []
stopped = False

while not stopped:
    e= int(input("what is expense (type 0 to stop )"))
    if e!=0:
        exp.append(e)
    else:
        stopped= True    
print(exp)
print("Total expense :",sum(exp))
print("Max expense :",max(exp))       
print("Min expense :",min(exp))