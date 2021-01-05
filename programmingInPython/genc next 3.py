#import sys
cse=int(input("Enter the no of students placed in CSE:"))
ece=int(input("Enter the no of students placed in ECE:"))
mech=int(input("Enter the no of students placed in MECH:"))
if cse==ece and ece==mech:
    print("None of the departments got highest placement")
elif cse<0 or ece<0 or mech<0:
    print("Invalid Input")
    
else:
    
    print("Highest Placement")
    m=max(cse,ece,mech)
    if m==cse:
        print("CSE")
    if m==ece:
        print("ECE")
    if m==mech:
        print("MECH")
    
