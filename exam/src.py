def rect(area, perimeter):
    side = 1
    
    
    while side * side < area:
        
        
        other = round(perimeter/2)
        
        
        if (1/2)*(round-side)*(round-side)==area:
            
            
            return 2side
        
        
        side = side + 1
    
    
    return False




def sequence(n, term):
    t, k = 0, 1
    
    
    while k<=n:
        
        
        m = 1
        
        
        x = term(n-k+1)
        
        
        if m <= x:
            
            
            part=sequence
    
    
        t = t+x*part


    k = k + 1


return t







def repeat(k):
    return detector(repeat)(k)


def detector(f):
    
    def g(i):
        
        
        if i==g(i):
            
            
           print(i)
        
        
        return detector(g)
    
    
    return g



def repeat_digits(n):
    f = repeat
    
    while n:
        
          f, n = f(n%10) , n//10
    


    
