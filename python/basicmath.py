#count no of digits
def code1(n):
    a=n
    count=0
    while(a>0):
        rem=a%10
        a=a//10
        count+=1
        print(rem,end=" ")
    print(count)
# reverse a number
def code2(n):
    a=n
    rev=0
    while(a>0):
        rem=a%10
        rev=((rev*10)+rem)
        a=a//10
    print(rev)
#palindrome or not
def code3(n):
    a=n
    rev=0
    while(a>0):
        rem=a%10
        rev=((rev*10)+rem)
        a=a//10
    if(rev==n):
        print("palindrome")
    else:
        print("not a palindrome")
# prime or
def code4(n):
    count=0
    for i in range(1,n):
        if (n%1==0 and n%i==0):
            count+=1
    if(count==1):
        print("prime")
    else:
        print("not a prime")          
# armstrong number
def code5(n):
    num=n
    sum=0
    while n>0:
        rem=n%10
        sum+=rem*rem*rem;
        n=n//10
    if sum==num:
        print(" armstrong number")
    else:
        print("not an armstrong number")
# print all the divisors
def code6(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i, end=" ")
#  gcd or hcf of a number
def code7(n1,n2):
    gcd=1
    for i in range(1,min(n1,n2)+1):
        if(n1%i==0 and n2%i==0):
            gcd=i
    print("gcd of the numbers is:",gcd)        
code7(1,1) 
