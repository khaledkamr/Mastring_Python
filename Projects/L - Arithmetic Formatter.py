
def arithmetic_arranger(*problem):

    for p in problem:

        if (p.find('+') != -1):
            num1 = p[0 : p.find('+')].strip()
            num2 = p[p.find('+')+1 : ].strip()
            res = int(num1) + int(num2)
        else:
            num1 = p[0 : p.find('-')].strip()
            num2 = p[p.find('-')+1 : ].strip()
            res = int(num1) - int(num2)
        
        print("  ", end = "")

        if (len(num1) < len(num2)): # 3 < 1
            print(" " * abs(len(num1) - len(num2)), end = "")
            print(num1)   
        else:
            print(num1)
        
        if (p.find('+') != -1):
            print("+ ", end = "")
        else:
            print("- ", end = "")

        if (len(num2) < len(num1)): # 3 < 2
            print(" " * abs(len(num1) - len(num2)), end = "")
            print(num2)
        else:
            print(num2)

        print("-" * (max(len(num1), len(num2)) + 2))

        res = str(res)

        if (len(res) > max(len(num1), len(num2))): # 2 > 3
            print(f" {res}")
        
        elif (len(res) < max(len(num1), len(num2))):
            print("  ", end = "")
            print(" " * abs(len(str(max(len(num1), len(num2)))) - len(res)), end = "")
            print(res)
        else:
            print(f"  {res}")
        print("\n")

n = int(input("How many problems you got : (1-5) "))

while n > 5 : 
    print("Too many problems.")
    n = int(input("enter the number of problems again : "))

mylist = []

while (n):
    eq = input("enter the problem : ").strip()

    while (eq.find('*') != -1 or eq.find('/') != -1):
        print("Operator must be '+' or '-'.")
        eq = input("enter the problem again : ")

    if (eq.find('+') != -1):
        num1 = eq[0 : eq.find('+')].strip()
        num2 = eq[eq.find('+')+1 : ].strip()
    else:
        num1 = eq[0 : eq.find('-')].strip()
        num2 = eq[eq.find('-')+1 : ].strip()

    while (len(num1) > 4 or len(num2) > 4):
        print("Numbers cannot be more than four digits.")
        eq = input("enter the problem again : ") 

        if (eq.find('+') != -1):
            num1 = eq[0 : eq.find('+')].strip()
            num2 = eq[eq.find('+')+1 : ].strip()    
        else:
            num1 = eq[0 : eq.find('-')].strip()
            num2 = eq[eq.find('-')+1 : ].strip()
    
    # try:
    #     int(num1)
    #     int(num2)
    # except :
    #     print("Numbers must only contain digits.")
    #     eq = input("enter the problem again : ")

    #     if (eq.find('+') != -1):
    #         num1 = eq[0 : eq.find('+')].strip()
    #         num2 = eq[eq.find('+')+1 : ].strip()
       
    #     elif (eq.find('-') != -1):
    #         num1 = eq[0 : eq.find('-')].strip()
    #         num2 = eq[eq.find('-')+1 : ].strip()

    mylist.append(eq)
    n -= 1

arithmetic_arranger(*mylist)
