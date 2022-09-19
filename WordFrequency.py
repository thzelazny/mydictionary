

infile=open("sometext.txt","r")

readfile=infile.read()


mylist=readfile.split(" ")
mydict={}
for term in mylist:
    term=term.lower()
    term=term.replace(".","")
    term=term.replace(",","")
    term=term.replace("\n","")
    count=mylist.count(term)
    mydict[term]=count

print(mydict)





