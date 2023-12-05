a=int(input("Enter number of years:"))
temp=0

for i in range(1,13):
    a=int(input(f"Enter temprature for month{i}:")) 
    if(a>temp):
        temp=a
    else:
        a=a      

print("This is the highest temprature in this year",temp) 