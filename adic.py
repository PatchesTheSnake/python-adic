"""provides support of the p-adicts in python"""
class p_adic():
    """provides support of the p-adicts in python"""
    def __init__(self,n):
        """creates a new p-adic number with n, a prime adic number"""
        #check if number is prime
        if n==1:
            raise TypeError(str(n)+" is not a prime number")
        else:
            for i in range(2, (n//2)+1):
                if num%i ==0:
                    raise TypeError(str(n)+" is not a prime number")
