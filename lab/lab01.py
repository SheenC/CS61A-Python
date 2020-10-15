"""Lab 1: Expressions and Control Structures"""

# Q3
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return (x>0 and y>0) # You can replace this line!

# Q4
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    t=n
    k=0
    i=0
    sum=0

    while (t//10 > 0):
          k += 1
          t //= 10

    
    while (i<=k):
          sum += (n % 10)
          n //= 10
          i += 1
 
    return sum

    
          
    


    
