fname=input("Enter file name to open:")
fr=open(fname)
mail_counter=dict()
for line in fr:

    if line.startswith("From"):
        line=line.split()
        sender=line[1]  
        mail_counter[sender]=mail_counter.get(sender,0)+1
    
max_sender=None
count_max=0
if mail_counter[sender]>count_max:
    mail_counter[sender]=count_max
    max_sender=sender
print(max_sender,count_max)