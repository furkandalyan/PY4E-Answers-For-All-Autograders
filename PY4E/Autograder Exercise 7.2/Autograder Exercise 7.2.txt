count=0
toplam=0
fname=input("Enter file name to open:")
fr=open(fname)
for line in fr:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        sira=line.find("0")
        sayi=line[sira:]
        sayi=float(sayi)
        toplam=toplam+sayi
        
print("Average spam confidence:",toplam/count)