# from math import sqrt

# num=int(input("Enter a number:"))

# if num>1:
#     for i in range(2,int(sqrt(num))+1):
#         if (num%i)==0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
    
  
  
# def primeseive(n):
#     prime=[True for i in range(n+1)]
#     current=2
#     while(current*current<=n):
#         if (prime[current]==True):
#             for i in range(current**2,n+1,current):
#                 prime[i]=False
#         current+=1
#     prime[0]=False
#     prime[1]=False
#     for p in range(n+1):
#         if prime[p]:
#                 print(p)

# n=int(input("Enter a number:"))

# primeseive(n)





#prints numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for multiples of both, print "FizzBuzz.


for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz",i)
    elif i%3==0:
        print("Fizz",i)  
    elif i%5==0:
        print("Buzz",i)
    else:
        print(i)