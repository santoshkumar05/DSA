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
# prime or not
def code4(n):
    count=0
    for i in range(1,n):
        if (n%1==0 and n%i==0):
            count+=1
    if(count==1):
        print("prime")
    else:
        print("not a prime")          
#  
code4(41) 
