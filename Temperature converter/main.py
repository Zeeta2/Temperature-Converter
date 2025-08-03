print("Enter the type of the temperature \n1.Celsius \n2.Fahrenheit \n3.Kelvin")
options=int(input("Enter the temperature's serial number you want to enter: "))
temp=int(input("Enter the temperature: "))
toconvert=int(input("Enter the temperature's serial number you want to convert to: "))
if 1<= toconvert <=3 and 1<= options <=3:
    if options==1:
        if toconvert==1:
            print("already the temperature is in the required format")
        if toconvert==2:
            print(round((temp*9/5)+32,2),"F")
        else:
            print(round(temp+273.15,2),"K")
    if options==2:
        if toconvert==1:
            print(round((temp-32)*5/9,2),"C")
        if toconvert==2:
            print("already the temperature is in the required format")
        else:
            print(round((temp-32)*5/9+273.15,2),"K")
    if options==3:
        if toconvert==1:
            print(round(temp-273.15,2),"C")
        if toconvert==2:
            print(round((temp-273.15)*9/5+32,2),"F")
        else:
            print("already the temperature is in the required format")
else:
    print("Invalid serial number entered")        

 