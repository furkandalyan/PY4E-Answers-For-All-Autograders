count=0

fname=input("Enter file name to open:")
fr=open(fname)
for line in fr:
    if line.startswith("From "):
        count=count+1
        line=line.split()
        print(line[1])
print("There were",count,"lines in the file with From as the first word")
    