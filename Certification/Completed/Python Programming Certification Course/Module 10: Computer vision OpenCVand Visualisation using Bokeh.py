#1.Write a program to fetch hyperlinks from any website which user enters.
import requests
from bs4 import BeautifulSoup
url="https://python-visualization.github.io/folium/modules.html#module-folium.map"
r=requests.get(url)
c=r.content
soup=BeautifulSoup(c,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

#2.Write  a  program  to  download  all  the  videos  from  youtube.com    for  django  from the hyperlink given below
#I am in Europe which forbid to download youtube video and youtube is now https

#3.Create a csv file with name and hyperlink after fetching it from the web page
import requests
from bs4 import BeautifulSoup
import csv

fc=csv.writer(open('innovators.csv', 'w'))
fc.writerow(["Name","link"])

f=open("/Users/prateekb/Downloads/PythonPractice/Machine Learning/test.html","r")
c=f.read()
soup=BeautifulSoup(c,'html.parser')
for link in soup.find_all('a'):
    names=link.contents[0]
    href=link.get('href')
    fc.writerow([names,href])

#4.from the question above, fetch only the hyperlinks
import requests
from bs4 import BeautifulSoup
import csv

f=open("/Users/prateekb/Downloads/PythonPractice/Machine Learning/test.html","r")
c=f.read()
soup=BeautifulSoup(c,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

#5.from the question above, fetch -names, years, positions, parties, states, congress, fullLink
#Not able to do

#6
#i)Read  the  page  using  BeautifulSoup  and  show  it  in  well  formatted  indented manner.
import requests
from bs4 import BeautifulSoup
import csv
f=open("/Users/prateekb/Downloads/PythonPractice/Machine Learning/WS.html","r")
c=f.read()
soup=BeautifulSoup(c,'html.parser')
print(soup.prettify())

# ii)Print the b tag from the page
import requests
from bs4 import BeautifulSoup
import csv
f=open("/Users/prateekb/Downloads/PythonPractice/Machine Learning/WS.html","r")
c=f.read()
soup=BeautifulSoup(c,'html.parser')
print(soup.find_all('b'))

# iii)Print all the tags that starts from b
import requests
from bs4 import BeautifulSoup
import csv
import re
f=open("/Users/prateekb/Downloads/PythonPractice/Machine Learning/WS.html","r")
c=f.read()
soup=BeautifulSoup(c,'html.parser')
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# iv)Print text from the tags having 'title' and 'p'. by using lists
import requests
from bs4 import BeautifulSoup
import csv
import re
doc = ['<html><head><title>Page title</title></head>','<body><p id="firstpara" align="center">This is paragraph <b>one</b>.','<p id="secondpara" align="blah">This is paragraph <b>two</b>.','</html>']
soup=BeautifulSoup(''.join(doc),'lxml')
#for tag in soup.find_all(re.compile("p|title")):
    #print(tag.string)

for tag in soup.find_all(['title','p']):
    print(tag.text.strip())
# v)Print text from the tags having 'title' and 'p'. by using dictionaries
from bs4 import BeautifulSoup
doc = ['<html><head><title>Page title</title></head>','<body><p id="firstpara" align="center">This is paragraph <b>one</b>.','<p id="secondpara" align="blah">This is paragraph <b>two</b>.','</html>']
soup = BeautifulSoup(''.join(doc), 'lxml')
for tag in soup.find_all(['title','p']):
    print(tag.text)

#vi)Print all the tag names present in the page
import requests
from bs4 import BeautifulSoup
import csv
import re
doc = ['<html><head><title>Page title</title></head>','<body><p id="firstpara" align="center">This is paragraph <b>one</b>.','<p id="secondpara" align="blah">This is paragraph <b>two</b>.','</html>']
soup=BeautifulSoup(''.join(doc),'lxml')
#for tag in soup.find_all(re.compile("p|title")):
    #print(tag.string)

for tag in soup.find_all():
    print(tag.name)
#vii)Print the complete tag that have two, and only two, attributes
import requests
from bs4 import BeautifulSoup
import csv
import re
doc = ['<html><head><title>Page title</title></head>','<body><p id="firstpara" align="center">This is paragraph <b>one</b>.','<p id="secondpara" align="blah">This is paragraph <b>two</b>.','</html>']
soup=BeautifulSoup(''.join(doc),'lxml')
#for tag in soup.find_all(re.compile("p|title")):
    #print(tag.string)

for tag in soup.find_all():
    if(len(tag.attrs)==2):
        print(tag.name)
#viii)Print the tags that have one-character names and no attributes
import requests
from bs4 import BeautifulSoup
import csv
import re
doc = ['<html><head><title>Page title</title></head>','<body><p id="firstpara" align="center">This is paragraph <b>one</b>.','<p id="secondpara" align="blah">This is paragraph <b>two</b>.','</html>']
soup=BeautifulSoup(''.join(doc),'lxml')
#for tag in soup.find_all(re.compile("p|title")):
    #print(tag.string)

for tag in soup.find_all():
    if(len(tag.attrs)==0 and len(tag.name)==1):
        print(tag.name)

#ix)Print all the tags which have a value of "center" for their "align" attribute
import requests
from bs4 import BeautifulSoup
import csv
import re
doc = ['<html><head><title>Page title</title></head>','<body><p id="firstpara" align="center">This is paragraph <b>one</b>.','<p id="secondpara" align="blah">This is paragraph <b>two</b>.','</html>']
soup=BeautifulSoup(''.join(doc),'lxml')
for tag in soup.find_all(align="center"):
    print(tag.name)

# x)From the xml content'<person name="Bob"><parent rel="mother" name="Alice">'Print the attributes having "name" as "Alice"
import requests
from bs4 import BeautifulSoup
import csv
import re
doc = ['<person name="Bob"><parent rel="mother" name="Alice">']
soup = BeautifulSoup(''.join(doc), 'lxml')

for tag in soup.find_all(attrs={"name":"Alice"}):
    print(tag.name)