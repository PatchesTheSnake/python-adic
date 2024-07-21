import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)
"""provides support of the p-adic numbers in python"""
class p_adic():
    """creates a new p-adic number with n, a prime adic number with a value of the number"""
    def __init__(self,n,value):
        """creates a new p-adic number with n, a prime adic number with a value of the number"""
        #check if number is prime
        if n==1:
            raise TypeError(str(n)+" is not a prime number")
        else:
            for i in range(2, (n//2)+1):
                if n%i ==0:
                    raise TypeError(str(n)+" is not a prime number")
        #make sure value is able to be converted to int
        if not isinstance(value,int)or isinstance(value,float):
            raise TypeError("type of value must be int or float not "+str(type(value)))
        self.base=n#get bases set up
        self.value=value
        self.adj_value=int2base(value,n) 
        if isinstance(value,int) and value>-1:
            self.rep_value="0"
            self.end_value=str(self.adj_value)
        else:
            pass
