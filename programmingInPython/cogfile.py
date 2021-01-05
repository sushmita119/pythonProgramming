lines=["this is first line\n","this is second line\n","this is third line\n"]
with open("D:\python\exam1.txt","w")as file1:
    for line in lines:
        file1.write(line)
