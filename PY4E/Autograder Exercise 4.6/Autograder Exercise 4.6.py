def computepay(hours,rate):
    if hours<=40:
        pay=hours*rate
    elif hours>40.0:
        pay=(40.0*rate)+((hours-40.0)*(rate*1.5))
        return pay
       
    


ahours=float(input("Enter hours:"))
arate=float(input("Enter rate:"))
pay=computepay(ahours,arate)
print("Pay",pay)


    
    
    
        
   
   
  
