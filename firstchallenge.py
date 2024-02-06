x = "Bill"
y = "Tip"
z= "Total Amount Paid"

x = 3 
y = 0.15*x
z= x + y

def TotalAmount():
    print(z)

TotalAmount()\

service =  input("How was our service?")

if service == ("Bad"):
    print( "0% Tip" )
    y= x
elif service == ("Mid"):
    print("10% Tip")

elif service == ("Good"):
    print ("20% Tip")
    y = x*0.2

elif service == ("Great/Amazing!"):
    print ("27.5% Tip")


