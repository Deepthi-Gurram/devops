n=int(input("enter prime numbers:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
    if c==2:
        print("prime")
    else:
        print("not prime")
n=int(input("enter even numbers"))
for i in range (1,n+1):
    if i%2==0:
        print(i)
n=int(input("enter number of factorials"))
facto=1
for i in range (1,n+1):
    facto=facto+1
    print(facto)
n=int(input("enter a number for table:"))
for i in range (1,11):
    print(n*i)