mylist=[]

fname=input("Enter file name to open:")
fr=open(fname)
for line in fr:
    words=line.split()
    for word in words:
        if word not in mylist:
            mylist.append(word)
    mylist.sort()
print(mylist)
    




