
def arithmetic_arranger(*problem):

    for p in problem:
        if (p.find('+') != -1):
            num1 = p[0 : p.find('+')]
            num2 = p[p.find('+')+1 : ]
            res = int(num1) + int(num2)

        elif (p.find('-') != -1):
            num1 = p[0 : p.find('-')]
            num2 = p[p.find('-')+1 : ]
            res = int(num1) - int(num2)
        
        print("  ", end = "")

        if (len(num1) < len(num2)): # 2 < 3
            print(" " * abs(len(num1) - len(num2)), end = "")
            print(num1)   

        else:
            print(num1)
        
        print("+ ", end = "")

        if (len(num2) < len(num1)): # 3 < 2
            print(" " * abs(len(num1) - len(num2)), end = "")
            print(num2)

        else:
            print(num2)

        print("-" * (max(len(num1), len(num2)) + 2))

        res = str(res)

        if len(res) > max(len(num1), len(num2)):
            print(f" {res}")

        else:
            print(f"  {res}")
        

n = int(input("How many problems you got : (1-5) "))

while n > 5 : 
    print("sorry, the maximum number of problems is 5!")
    n = int(input("enter the number of problems again : "))

mylist = []

while (n):
    eq = input("enter the problem : ").strip()

    while(eq.find('*') != -1 or eq.find('/') != -1):
        print("only + and - opration is allowed!")
        eq = input("enter the problem again : ")

    mylist.append(eq)
    n -= 1

arithmetic_arranger(*mylist)
