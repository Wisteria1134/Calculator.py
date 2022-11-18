#AppliedSign should be 1-4 [1=+,2=-,3*,4=/]
AppliedSign = 0
Number1 = 0
Number2 = 0
outcome = 0
#Fuctions
def ADD():
    return int(Number1) + int(Number2)
    
def SUB():
    return int(Number1) - int(Number2)
    
def MUL():
    return int(Number1) * int(Number2)
    
def DIV():
    return int(Number1) / int(Number2)
    

Number1 = input("First number? ")
Number2 = input("Second number? ")

print("1. Add")
print("2. Subracte")
print("3. Multiply")
print("4. Divide")
AppliedSign = str(input("Choose an operation: "))
if AppliedSign == '1':
    print(ADD())
elif AppliedSign == '2':
    print(SUB())
elif AppliedSign == '3':
    print(MUL())
elif AppliedSign == '4':
    print(DIV())
else:
    print("Entered Input Is Not Valid")