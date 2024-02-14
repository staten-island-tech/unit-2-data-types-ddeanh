""" number = float(input("What is your number?"))
number2 = float(input("What is your second number?"))

num = int(number)
num2 = int(number2)
factors = []
for i in range(1, number+1):
    if num%1 == 0 and num2%i ==0:
        
        
        
        for i in factors:
            print (i) """

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

result = gcd(num1, num2)

print(f"The GCF of {num1} and {num2} is {result}")

