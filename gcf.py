num1 = int(input("Put your 1st number here:"))
num2 = int(input("Put your 2nd number here:"))

def gcf(x,y):
    if x > y:
        less = y
    else:
        less  = x
    for i in range(1,less+1):
        if((x % i ==0)) and ((y % i ==0)):
            gcf = i
    return gcf


print("THE GCF OF YOUR TWO NUMBERS IS", gcf(num1, num2 ))
