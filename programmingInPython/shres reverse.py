def rev(s):
    l=[]
    word=s.split(' ')
    rev_sen=' '.join(reversed(word))
    print("'"+rev_sen+"'")
    
s=input()
rev(s)
