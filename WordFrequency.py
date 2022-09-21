

infile=open("sometext.txt","r")

readfile=infile.read()


mylist=readfile.split(" ")
mydict={}
for term in mylist:
    term=term.lower()
    term=term.replace(".","")
    term=term.replace(",","")
    term=term.replace("\n","")
    if term in mydict:
        mydict[term]=mydict[term]+1
    else:
        mydict[term]=1

print(mydict)





