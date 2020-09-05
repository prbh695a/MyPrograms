import sys
from googlesearch import search
query=sys.argv[1]
urlResult=[]
searchRes=search(query,tld='com',lang = 'en',num = 10,start = 0,stop = None,pause = 2.0)
print("the top links are...")
for i in searchRes:
    urlResult.append(i)
    print(i)
