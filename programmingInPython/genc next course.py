print("Enter the number of courses")
l=[]
n=int(input())
if n>20 or n<=0:
    print("Invalid Range")
else:
    print("Enter the courses")
    for i in range(n):
        
        l.append(input())
print("Enter course to be searched")
course = input()
if course in l:
    print(course + " is available")
else:
    print(course + " is not availabe") 
    
