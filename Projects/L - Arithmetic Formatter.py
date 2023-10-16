

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

        if (len(num1) < len(num2)): 
            print(" " * abs(len(num1) - len(num2)), end = "")
            print(num1)   
        else:
            print(num1)
        
        if (p.find('+') != -1):
            print("+ ", end = "")
        else:
            print("- ", end = "")

        if (len(num2) < len(num1)): 
            print(" " * abs(len(num1) - len(num2)), end = "")
            print(num2)
        else:
            print(num2)

        print("-" * (max(len(num1), len(num2)) + 2))

        res = str(res)

        if (len(res) > max(len(num1), len(num2))): 
            print(f" {res}")
        
        elif (len(res) < max(len(num1), len(num2))):
            print("  ", end = "")
            print(" " * abs(len(str(max(len(num1), len(num2)))) - len(res)), end = "")
            print(res)
        else:
            print(f"  {res}")
        print("\n")

def check_digit(x, y):

    for d1 in x:
        for d2 in y:
            if ((ord(d1) >= 97 and ord(d1) <= 122) or (ord(d1) >= 65 and ord(d1) <= 90)
                or (ord(d2) >= 97 and ord(d2) <= 122) or (ord(d2) >= 65 and ord(d2) <= 90)):

                print("Numbers must only contain digits!")
                eq = input("enter the problem again : ")

                if(eq.find('+') != -1):
                    num1 = eq[0 : eq.find('+')].strip()
                    num2 = eq[eq.find('+') +1 : ].strip()
                else:
                    num1 = eq[0 : eq.find('-')].strip()
                    num2 = eq[eq.find('-') + 1 : ].strip()
                
                return check_digit(num1, num2) 
            
    return eq

n = int(input("How many problems you got : (1-5) "))

while (n > 5) : 
    print("Too many problems.")
    n = int(input("Enter the number of problems again : "))

mylist = []

while (n):
    eq = input("Enter the problem : ").strip()

    while (eq.find('*') != -1 or eq.find('/') != -1):
        print("Operator must be '+' or '-'!")
        eq = input("Enter the problem again : ")

    if (eq.find('+') != -1):
        num1 = eq[0 : eq.find('+')].strip()
        num2 = eq[eq.find('+')+1 : ].strip()
    else:
        num1 = eq[0 : eq.find('-')].strip()
        num2 = eq[eq.find('-')+1 : ].strip()

    while (len(num1) > 4 or len(num2) > 4):
        print("Numbers cannot be more than four digits.")
        eq = input("Enter the problem again : ") 

        if (eq.find('+') != -1):
            num1 = eq[0 : eq.find('+')].strip()
            num2 = eq[eq.find('+') + 1 : ].strip()    
        else:
            num1 = eq[0 : eq.find('-')].strip()
            num2 = eq[eq.find('-') + 1 : ].strip()
    
    eq = check_digit(num1, num2)

    mylist.append(eq)
    n -= 1

arithmetic_arranger(*mylist)


