largest_number=None
smallest_number=None
while True:
    num=input("Enter number:")
    if num=="done":
        break
    
    try:
        num=int(num)
        if largest_number is None or largest_number<num:
            largest_number=num
        if smallest_number is None or smallest_number>num:
            smallest_number=num
    except:
        print("Invalid input")
print("Maximum is",largest_number)
print("Minimum is",smallest_number)