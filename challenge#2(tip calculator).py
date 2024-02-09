x = "Bill"
y = "Tip"
z= "Total Amount Paid"
total = 0
tip = 0


x = float(input("How much was your meal?"))




service =  input("How was our service?")




if service == ("Bad"):
    print( "0% Tip" )
    tip = x
elif service == ("Mid"):
    print("10% Tip")
    tip = x * 0.1
elif service == ("Good"):
    print ("20% Tip")
    tip = x*0.2

elif service == ("Great"):
    print ("27.5% Tip")
    tip= x*.275

elif service == ("Amazing"):
    print ("27.5% Tip")
    tip = x*.275

total = x + tip


print (total) 




