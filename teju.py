def checkAnagram(A,B):
    if len(A) !=len(B):
        return False
    A=sorted(A)
    B=sorted(B)
    if A==B:
        return True
    else:
        return False

def isArmstrong(n):
    if n<0:
        return False
    temp=n
    digits=len(str(n))
    total=0
    while temp>0:
        digit=temp%10
        total=total+digit**digits
        temp=temp//10
    return total==n

def next_prime(n):
    num=n+1
    while True:
        prime=True
        if num<=1:
            prime=False
        else:
            for i in range(2,num):
                if num%i==0:
                    prime=False
                    break
            else:
                return num
    num+=1



