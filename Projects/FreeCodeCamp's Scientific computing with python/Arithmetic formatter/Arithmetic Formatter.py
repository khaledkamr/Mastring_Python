
def arithmetic_arranger(*problem):

    num1 = []
    num2 = []
    op = []
    res = []

    for p in problem:

        if (p.find('+') != -1):
            n1 = p[0 : p.find('+')].strip()
            n2 = p[p.find('+') + 1 : ].strip()
            operator = '+'
            result = int(n1) + int(n2)
        else:
            n1 = p[0 : p.find('-')].strip()
            n2 = p[p.find('-') + 1 : ].strip()
            operator = '-'
            result = int(n1) - int(n2)
        
        num1.append(n1)
        num2.append(n2)
        op.append(operator)
        res.append(str(result))
    
    for i in range(len(num1)):
        print("  ", end = "")
        if(len(num1[i]) < len(num2[i])):
            print(" " * abs(len(num1[i]) - len(num2[i])), end = "")
            print(num1[i], end = "    ")
        else:
            print(num1[i], end = "    ")

    print(" ")
    
    for i in range(len(num2)):
        print(f"{op[i]} ", end = "")
        if(len(num2[i]) < len(num1[i])):
            print(" " * abs(len(num1[i]) - len(num2[i])), end = "")
            print(num2[i], end = "    ")
        else:
            print(num2[i], end = "    ")

    print(" ")

    for i in range(len(op)):
        print("-" * (max(len(num1[i]), len(num2[i])) + 2), end = "    ")

    print(" ")

    for i in range(len(res)):
        if(len(res[i]) > max(len(num1[i]), len(num2[i]))):
            print(f" {res[i]}", end = "    ")

        elif (len(res[i]) < max(len(num1[i]), len(num2[i]))):
            print("  ", end = "")
            print(" " * abs(max(len(num1[i]), len(num2[i])) - len(res[i])), end = "")
            print(res[i], end = "    ")
        else:
            print(f"  {res[i]}", end = "    ")
    
    print(" ")

def check_digit(x, y, op):

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
                
                return check_digit(num1, num2, op) 
            
    return f"{x}{op}{y}"

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
    
    if (eq.find('+') != -1):
        eq = check_digit(num1, num2, '+')
    else:
        eq = check_digit(num1, num2, '-')

    mylist.append(eq)
    n -= 1

arithmetic_arranger(*mylist)


