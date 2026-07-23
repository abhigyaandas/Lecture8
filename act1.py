print("Enter all of your grades")

Sub1=int(input("Math: "))
Sub2=int(input("Spanish: "))
Sub3=int(input("PE: "))
Sub4=int(input("English: "))
Sub5=int(input("History: "))

Total=int(Sub1+Sub2+Sub3+Sub4+Sub5)
av=int(Total/5)

ValidRange=range(0, 101)

if av not in ValidRange:
    print("Invalid range")
elif av in range(91, 101):
    print("Your grade is an A")
elif av in range(81, 91):
    print("Your grade is a B")
elif av in range(71, 81):
    print("Your grade is a C")
elif av in range(51, 71):
    print("Your grade is a D")
else:
    print("You have failed F")