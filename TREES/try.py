def category(entry):
    digit_index = 0
    for character in entry:
        if character.isdigit():
            digit_index = entry.index(character)
            break
    category = entry[1:(digit_index - 2)]
    return category


def spending(entry):
    digit_index = 0
    for character in entry:
        if character.isdigit():
            digit_index = entry.index(character)
            break
    spending = entry[digit_index:]
    return int(spending)

def spli(l):
    spend = l[-1]
    print(int(spend))
    return int(spend)
def cato(l):
    spend = l[-1]
    s=""
    l.remove(spend)
    s=s.join(l)
    s2=""
    for i in range(1,len(l)-1):
        s2=s2 + " " +s[i]

    print(s2)
    return s2
s=input()
cat = category(s)
spend = spending(s)
print(cat,spend,"l")
d={"personal care":[],"food":[]}
for index,val in d.items():
    print(index)
    if index ==cat:
        val.append(spend)
print(d)

