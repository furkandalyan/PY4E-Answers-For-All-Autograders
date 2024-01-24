normalhours=input("Enter hours:")
nh=float(normalhours)
normalrate=input("Enter rate:")
nr=float(normalrate)
if nh>40:
    normalpay=(nr*40.0)
    extrapay=(nh-40.0)*(nr*1.5)
    pay=normalpay+extrapay
    print(pay)