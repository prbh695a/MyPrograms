
def LetterChanges(str):
    newstr= ""
    finalstr= ""
    for i in str:
        if i.isalpha():
            if i == "z":
                newstr = newstr + "a"
            else:
                newstr = newstr + chr(ord(i) + 1)
        else:
            newstr = newstr + i
    for i in newstr:
        if i in "a,e,i,o,u":
            finalstr=finalstr+i.upper()
        else:
            finalstr=finalstr+i
    return finalstr

# keep this function call here
print(LetterChanges("hello*3"))