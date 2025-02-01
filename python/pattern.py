#pattern 1
def pattern1(n):
    for i in range(1,n):
        for j in range(1,n-i):
            print(j,end=" ")
        print()
#pattern 2
def pattern2(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end=" ")
        print()
#pattern 3
def pattern3(n):
    for i in range(0,n):
        for j in range(0,i):
            print("*",end=" ")
        print()
#pattern 4
def pattern4(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
        print()
#pattern 5
def pattern5(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(j,end=" ")
        print()
#pattern 6
def pattern6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(i,end=" ")
        print() 

pattern3(6)